
import os
os.chdir("C:/Users/yxhua/Desktop/IBI/IBI1_2024-25/IBI1_2024-25/Practical14")

import xml.dom.minidom
import xml.sax

from datetime import datetime

def analyze_with_dom(filename):
    
    start_time = datetime.now()
    
    namespace_stats = {
        'molecular_function': {'max_term': '', 'count': 0},
        'biological_process': {'max_term': '', 'count': 0},
        'cellular_component': {'max_term': '', 'count': 0}
    }
    
    dom_tree = xml.dom.minidom.parse("go_obo.xml")
    collection = dom_tree.documentElement
    terms = collection.getElementsByTagName("term")
    
    for term in terms:

        namespace_elem = term.getElementsByTagName('namespace')
        namespace = namespace_elem[0].childNodes[0].data.strip()

        name_elem = term.getElementsByTagName('name')
        term_name = name_elem[0].childNodes[0].data.strip() if name_elem and name_elem[0].childNodes else "Unknown"
        
        is_a_elements = term.getElementsByTagName('is_a')
        count = len(is_a_elements)

        if count > namespace_stats[namespace]['count']:
            namespace_stats[namespace]['count'] = count
            namespace_stats[namespace]['max_term'] = term_name
    
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    
    return namespace_stats, time_taken

class GOTermHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_tag = ""
        self.current_namespace = ""
        self.current_name = ""
        self.is_a_count = 0
        
        self.namespace_stats = {
            'molecular_function': {'max_term': '', 'count': 0},
            'biological_process': {'max_term': '', 'count': 0},
            'cellular_component': {'max_term': '', 'count': 0}
        }
    
    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'term':
            self.current_namespace = ""
            self.current_name = ""
            self.is_a_count = 0
    
    def characters(self, content):
        if self.current_tag == 'namespace':
            self.current_namespace += content.strip()
        elif self.current_tag == 'name':
            self.current_name += content.strip()
    
    def endElement(self, tag):
        if tag == 'is_a':
            self.is_a_count += 1
        elif tag == 'term' and self.current_namespace in self.namespace_stats:

            if self.is_a_count > self.namespace_stats[self.current_namespace]['count']:
                self.namespace_stats[self.current_namespace]['count'] = self.is_a_count
                self.namespace_stats[self.current_namespace]['max_term'] = self.current_name
        self.current_tag = ""

def analyze_with_sax(filename):

    start_time = datetime.now()
    
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    Handler = GOTermHandler()
    parser.setContentHandler(Handler)
    
    parser.parse(filename)
    
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    
    return Handler.namespace_stats, time_taken

def print_results(dom_stats, sax_stats, dom_time, sax_time):

    print("DOM:")
    for namespace, stats in dom_stats.items():
        print(f"Namespace: {namespace}")
        print(f"  term: {stats['max_term']}")
        print(f"  counts: {stats['count']}")
    print(f"Time cost: {dom_time:.6f}s")
    
    print("SAX:")
    for namespace, stats in sax_stats.items():
        print(f"Namespace: {namespace}")
        print(f"  term: {stats['max_term']}")
        print(f"  counts: {stats['count']}")
    print(f"Time cost: {sax_time:.6f}s")
    
    if dom_time < sax_time:
        print("DOM is faster!")
    elif sax_time < dom_time:
        print("SAX is faster!")
    else:
        print("The speed of DOM and SAX is the same!")

if __name__ == "__main__":
    filename = "go_obo.xml"  

    dom_stats, dom_time = analyze_with_dom(filename)

    sax_stats, sax_time = analyze_with_sax(filename)

    print_results(dom_stats, sax_stats, dom_time, sax_time)