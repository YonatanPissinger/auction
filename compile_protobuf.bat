rem pip install "betterproto[compiler]"
rem pip install flask
rem pip install requests
protoc -I . --python_betterproto_out=protobuf_out messages.proto
