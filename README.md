# ElectrumX_Compact_History_Service

- ElectrumX는 DB Flush를 할때 uint16(0~65535) 크기를 넘으면 Flush를 하지 않습니다. 이에 DB를 압축해줘야 하는데 이를 자동으로 모니터링하여 압축을 수행해 줍니다.
- ElectrumXはDB Flushする時にuint16(0~65535）のサイズを超えるとFlushをしません。なので、DBを圧縮する必要があります。このコードは自動的にモニタリングし、圧縮をします。
