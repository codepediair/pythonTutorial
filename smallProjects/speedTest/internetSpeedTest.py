import speedtest

s = speedtest.Speedtest()

print("Test Download Speed...")
download_res = s.download()/1024/1024
print(f"your download speed is : {download_res:.2f} mb/s")

print("Test upload Speed...")
upload_res = s.upload()/1024/1024
print(f"your upload speed is : {upload_res:.2f} mb/s")

print("Test Ping...")
ping_res = s.results.ping
print(f"your ping speed is : {ping_res:.2f} ms")
