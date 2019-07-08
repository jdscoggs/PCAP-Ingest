TABLES = {}
TABLES['container'] = (
    "CREATE TABLE `container` ("
    "  `container_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `create_date` date NOT NULL,"
    "  `file_name` varchar(41) NOT NULL,"
    "  `file_path` varchar(41) NOT NULL,"
    "  `sha1_hash` varchar(41) NOT NULL,"
    "  PRIMARY KEY (`container_id`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=1;")
TABLES['pcap_table'] = (
    "CREATE TABLE `pcap_table` ("
    "  `pcap_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `container_id` int(11) NOT NULL,"
    "  `pcap_name` varchar(41) NOT NULL,"
    "  `sha1_hash` varchar(41) NOT NULL,"
    "  PRIMARY KEY (`pcap_id`),"
    "  FOREIGN KEY (`container_id`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=1;")
TABLES['packet_table'] = (
    "CREATE TABLE `packet_table` ("
    "  `packet_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `pcap_id` int(11) NOT NULL,"
    "  `packet_name` varchar(41) NOT NULL,"
    "  `sha1_hash` varchar(41) NOT NULL,"
    "  `src_ip` varchar(41) NOT NULL,"
    "  `dst_ip` varchar(41) NOT NULL,"
    "  `src_port` varchar(41) NOT NULL,"
    "  `dst_port` varchar(41) NOT NULL,"
    "  `protocol` varchar(41) NOT NULL,"
    "  `payload` varchar(41) NOT NULL,"
    "  PRIMARY KEY (`packet_id`),"
    "  FOREIGN KEY (`pcap_id`)"
    "     REFERENCES `pcap_table` ('pcap_id')"
    ") ENGINE=InnoDB AUTO_INCREMENT=1;")
