
To create server skeleton and client stub:
`
wsdl2py wsdl.xml
`

Edit TimeServer_types.py

`
minOccurs=0
`

To run server:
` 
python TimeServer.py
`

To run client (server ip as args):
`
python TimeRequest.py 127.0.0.1
`
