'''
https://www.geeksforgeeks.org/layers-of-osi-model/
static page
dynamic page

frontend    <==> backend

UI   --1-->  Backend     --2-->  Database
     <--4--              <--3--
             C   S   D
             Controller .py
             Service    .py
             DAO        .py

Network : Interconnection of computers is called network  LAN WAN MAN
Client  : The computer that receive services
Server  : The computer that provide services

www.paytm.com  irctc


3 requirements to establish network :
    Hardware : Includes Computers,cables,modems,routers,hubs
    Software : Includes programs to communicate between server and client
    Protocol : Representing way to establish connections and
               helps to send and receive data in standard format

Browser  --> gmail server
client       server
www.gmail.com --> https://www.gmail.com  --> DNS 12.43.24.32  255*255*255*255

Client
    | |
Application Layer     Browsers, Skype Messenger etc.
    | |
Presentation Layer    Translation(ASCII), Encryption/Decryption, Compression
    | |
Session Layer          establishment of connection,
                       maintenance of sessions,
                       authentication and  security
    | |
Transport Layer        Segments End to End Delivery of the complete message
                       Segmentation  Flow & Error control
    | |
Network Layer           Routing Logical Addressing
                        transmission of data packet
    | |
Data link layer         Logical Link Control (LLC)
                        Media Access Control (MAC)
    | |
Physical Layer
    | |
  Server

Protocols:
--------------
TCP/IP and UDP(User Datagram Protocol)

TCP/IP : Transmission Control Protocol/Internet Protocol

            Application Layer
                |
                |           Data
                ^
            Transmission Protocol
                |
                |           Packets(group of data in bytes)
                ^
            Internet Protocol
                |
                |           Converts Packets into envelopes(Frames)
                |           Each frame contains
                |                       Packet  +
                |                       IP Address of Source computer +
                |                       IP Address of Destination computer +
                |                       Additional data
                ^
            Data Link Layer
                |
                |           Dispatches data to correct destination
                ^
            Physical Layer  Physically transmits the data on the network using hardware


IP Address : unique identification number given to each computer on the network
             Ex : www.google.com    # 216.58.194.197  (0-255) IPV4 / IPV6
                  localhost* /127.0.0.1/ 0.0.0.0

Domain name is automatically mapped to ip address is called DNS(Domain Naming Service)

Reserved port numbers and associated services :
-----------------------------------------------
Socket : Logical connecting point between client and server
         Each socket is given unique identification number called "port number"
         Port number can take 2 bytes(0 to 65535 bits) 2 bytes = 8 bits + 8 bits
Socket Programming : Establishing connection between client and server is called "Socket Programming"

Reserved port numbers and Associated Services:
----------------------------------------------
Port Number  Application/service
===========  ================================================
13           Date,Time services
21           FTP, to transfer files
22*          ssh, The Secure Shell (SSH) Protocol
23           Telnet,  provides remote login
25           SMTP,  which delivers mails
67           BOOTP, which provides configuration at boot time
80*          HTTP, which tranfser web PAGES
443*         HTTPS, which transfer web pages securely
'''