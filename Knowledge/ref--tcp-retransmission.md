---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Untitled
---

> For practice and visualization use [this pcap file](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmxoWjBleUk0NXljbzBfVkRCbjViNnZpNlIxQXxBQ3Jtc0tuamJuMDhyNGpTSWRoX19GNnJSdm9HanZ2NGMxRmFpdklOdnFNQnlVbW1Mal9uR0FvMktMLWhRN08wQ295X2NvUWRyY2pPalNhaGxiTFdyRURnUjNzOHFyYThES2FZTllXSkZDTUExMHJYbzNyeFRVYw&q=https%3A%2F%2Fpacketpioneer.com%2Fwp-content%2Fuploads%2FTCP-Retrans-and-Seq-Analysis.pcap_.zip&v=HTQLipAG27I)

When a client sends a packet (i.e initial "Client Hello"), but never gets a response back it starts a countdown onto itself and when the retransmission countdown expires it re-transmits the data
![[images/tcp_retransmission_initial_hello.png]]
Here the client had sent initial client hello
