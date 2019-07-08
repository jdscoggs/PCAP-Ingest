#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import mysql.connector, hashlib, tarfile, datetime, glob
from scapy.all import PcapReader
from scapy.all import *
from scapy.utils import *

def global_vars():
    global dest_path
    dest_path = '/Users/scogzy/Documents/work/new_pcaps/'

def get_tar_files():
    filenames = glob.glob('/Users/scogzy/Documents/work/tgzip/*')
    return filenames

def get_pcap_files():
    filenames = glob.glob('/Users/scogzy/Documents/work/tgzip/*')
    return pcap_filenames

def sha1_hash(filename):
    file_hash = hashlib.sha1(filename).hexdigest()
    return file_hash

def insert_container(tar_file_name):
    tar_file_hash = sha1_hash(filename)
    tar_file_split = tar_filename.split('/')
    tar_file_name = tar_file_split[6]
    tar_file_path = ('/' + tar_file_split[1] + '/' + tar_file_split[2] + '/' + tar_file_split[3] + '/' + tar_file_split[4] + '/' + tar_file_split[5] + '/')
    tar_filename_only = tar_filename[6]
    tar_insert_stmt = ("INSERT INTO container "
                  "(create_date, tar_file_name, tar_file_path, tar_sha1_hash)"
                  "VALUES (%(create_date)s, %(tar_file_name)s, %(tar_file_path)s, %(tar_sha1_hash)s)") 
    tar_insert_data = {
                  'create_date': datetime.date(2017, 12, 27),
                  'file_name': tar_file_name,
                  'file_path': tar_file_path,
                  'sha1_hash': tar_file_hash
                  }
    return tar_insert_stmt, tar_insert_data, tar_sha1_hash

def insert_pcap(filename, tar_sha1_hash):
    container_id = get_id('container_id', 'container', tar_sha1_hash, cursorA)
    unzipped_file = tarfile.open(filename, 'r:gz')
    for member_name in unzipped_file.getnames():
        unzipped_file.extract(member_name)
        file_hash = sha1_hash(member_name)
        member_name_split = member_name.split('/')
        pcap_name = member_name_split[2]
    pcap_insert_stmt = ("INSERT INTO pcap_table "
                  "(container_id, pcap_name, sha1_hash)"
                  "VALUES (%(container_id)s, %(pcap_name)s, %(sha1_hash)s)")
    pcap_insert_data = {
                       'container_id': container_id,
                       'pcap_name': pcap_name,
                       'sha1_hash': file_hash
                       }
    return pcap_insert_stmt, pcap_insert_data, pcap_name

def make_cursor():
    cnx = mysql.connector.connect(user='scogs', password='not42day', database='pcaps')
    cursorA = cnx.cursor()
    return cnx, cursorA

def get_packet_data(pcap_name, pcap_path):
    """
    scapy magic
    """
    for packet_name in get_packet_names(pcap_name, pcap_path):
        pcap_id = get_id('pcap_id', 'pcap_table', pcap_sha1_hash, cursorA)
        pcap_id = cursorA.fetchall()

def insert_packet(pcap_name, pcap_path, cursorA):
    for packet_name in get_packet_names(pcap_name, pcap_path):
        pcap_id = get_id('pcap_id', 'pcap_table', sha1_file_hash, cursorA)
        pcap_id = cursorA.fetchall()
    return
    
def get_id(column_name, table_name, select_name, cursorA):
    select_stmt = ("SELECT %s FROM %s "
                   "WHERE %s = %s" % (column_name, table_name, 'sha1_hash', "'" + select_name + "'"))
    cursorA.execute(select_stmt)
    selector_id = cursorA.fetchall()
    print(selector_id[0])
    return selector_id[0]

def main():
    global_vars()
    cnx, cursorA = make_cnx()
    for filename in get_tar_files():
        tar_insert_stmt, tar_insert_data, file_name = insert_container(filename)
        cursorA.execute(tar_insert_stmt, tar_insert_data)
        pcap_insert_stmt, pcap_insert_data, pcap_name = insert_pcap(filename, container_id)
        cursorA.execute(pcap_insert_stmt, pcap_insert_data)
    cnx.commit()
    packet_insert_stmt, packet_insert_data = insert_pcap(pcap_name, cursorA)
    return

def pcap_main(pcap_name):
    """
    WIP
    """
    global_vars()
    cnx, cursorA = make_cursor()
    for pcap_filename in get_pcap_files():
        pcap_id = get_id('pcap_id', 'pcap_table', pcap_sha1_hash, cursorA)
        pcap_id = cursorA.fetchall()
        pcap_insert_stmt, pcap_insert_data, pcap_name = insert_pcap(filename, container_id)

