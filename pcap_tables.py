CREATE TABLE `pictures` ( `picture_id` int(11) NOT NULL AUTO_INCREMENT, `create_date` date NOT NULL, `picture_name` varchar(14) NOT NULL, `picture_path` varchar(40) NOT NULL, `sha1_hash` varchar(41) NOT NULL, PRIMARY KEY (`picture_id`) ) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE `container` ( `container_id` int(11) NOT NULL AUTO_INCREMENT, `create_date` date NOT NULL, `file_name` varchar(100) NOT NULL, `file_path` varchar(100) NOT NULL, `sha1_hash` varchar(41) NOT NULL, PRIMARY KEY (`container_id`) ) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE `pcap_table` ( `pcap_id` int(11) NOT NULL AUTO_INCREMENT, `container_id` int(11) NOT NULL, `pcap_name` varchar(100) NOT NULL, `sha1_hash` varchar(41) NOT NULL, PRIMARY KEY (`pcap_id`), CONSTRAINT pcap_table_idfg FOREIGN KEY container(container_id) REFERENCES container(container_id) ) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE `packet_table` ( `packet_id` int(11) NOT NULL AUTO_INCREMENT, `pcap_id` int(11) NOT NULL, `packet_name` varchar(100) NOT NULL, `sha1_hash` varchar(41) NOT NULL, `src_ip` varchar(41) NOT NULL, `dst_ip` varchar(41) NOT NULL, `src_port` varchar(41) NOT NULL, `dst_port` varchar(41) NOT NULL, `protocol` varchar(41) NOT NULL, `payload` varchar(200) NOT NULL, PRIMARY KEY (`packet_id`), CONSTRAINT packet_id_idfg FOREIGN KEY pcap_table(pcap_id) REFERENCES pcap_table(pcap_id) ) ENGINE=InnoDB AUTO_INCREMENT=1;

ALTER TABLE pcap_table ADD FOREIGN KEY ('container') REFERENCES container('container_id');

ALTER TABLE packet_table ADD FOREIGN KEY ('pcap_table') REFERENCES pcap_table('pcap_id');


ALTER TABLE packet_table ADD CONSTRAINT packet_id_idfg FOREIGN KEY pcap_table(pcap_id) REFERENCES pcap_table(pcap_id);

ALTER TABLE pcap_table ADD CONSTRAINT pcap_id_idfg FOREIGN KEY container(container_id) REFERENCES container(container_id);
