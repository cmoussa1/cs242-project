import logging, sys

logging.disable(sys.maxsize)

import lucene
import json
import time
import os
from org.apache.lucene.store import MMapDirectory, SimpleFSDirectory, NIOFSDirectory
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader
from org.apache.lucene.search import IndexSearcher, BoostQuery, Query
from org.apache.lucene.search.similarities import BM25Similarity

#Prompt User for File Name for .json
file_path_name = input("Please enter the file name (must be .json): ")

with open(file_path_name, 'r', encoding="cp437") as json_file:
    data = json.load(json_file)

def create_index(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    store = SimpleFSDirectory(Paths.get(dir))
    analyzer = StandardAnalyzer()
    config = IndexWriterConfig(analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
    writer = IndexWriter(store, config)

    metaType = FieldType()
    metaType.setStored(True)
    metaType.setTokenized(False)

    contextType = FieldType()
    contextType.setStored(True)
    contextType.setTokenized(True)
    contextType.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

    for sample in data:
        name = sample['name']
        year = sample['year']
        biographical_information = sample['biographical_information']
        
        doc = Document()
        doc.add(Field('Title', str(name), metaType))
        doc.add(Field('Biographical Information', str(biographical_information), contextType))
        doc.add(Field('Year', str(year), metaType))
        writer.addDocument(doc)
    writer.close()


def retrieve(storedir, query, max_results=20, top_k=5):
    searchDir = NIOFSDirectory(Paths.get(storedir))
    searcher = IndexSearcher(DirectoryReader.open(searchDir))

    parser = QueryParser('Biographical Information', StandardAnalyzer())
    parsed_query = parser.parse(query)

    # fetch results (more than top-K in case of duplicates)
    topDocs = searcher.search(parsed_query, max_results).scoreDocs
    seen_players = {}  # track seen players and their scores
    topkdocs = []

    for hit in topDocs:
        doc = searcher.doc(hit.doc)
        name = doc.get("Title")
        year = int(doc.get("Year"))
        biographical_information = doc.get("Biographical Information")

        if name in seen_players:
            # we've seen this player before, so let's take the most recent year
            if (year > seen_players[name]['year']) or (hit.score > seen_players[name]['score']):
                seen_players[name] = {
                    "score": hit.score,
                    "name": name,
                    "year": year,
                    "text": biographical_information
                }
        else:
            seen_players[name] = {
                "score": hit.score,
                "name": name,
                "year": year,
                "text": biographical_information
            }

    # sort the results based on their scores
    topkdocs = list(seen_players.values())
    topkdocs = sorted(topkdocs, key=lambda x: x['score'], reverse=True)

    # only return the top K entries
    topkdocs = topkdocs[:top_k]

    print(topkdocs)

start_time = time.time()

lucene.initVM(vmargs=['-Djava.awt.headless=true'])
create_index('sample_baseball_index/')

end_time = time.time()
runtime = end_time - start_time
print("Index Building Runtime:", runtime, "seconds")

start_time = time.time()

user_input = input("Please enter search query: ")
print("You entered:", user_input)
print("Returning the top 5 associated documents")
retrieve('sample_baseball_index/', user_input)

end_time = time.time()
runtime = end_time - start_time
print("Search Query Runtime:", runtime, "seconds")
