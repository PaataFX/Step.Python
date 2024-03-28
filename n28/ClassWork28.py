# import time
# import threading


# run = True
# def printer():
#     counter = 0
#     while run:
#         time.sleep(1)
#         counter += 1
#         print(counter)


# first = threading.Thread(target=printer)
# first.start()


# input("Press Enter: ")
# run = False






# import time
# import threading

# run = True
# def printer(sec):
#     time.sleep(sec)
#     print("Done!")

# start = time.time()
# # printer()
# # printer()
# first = threading.Thread(target=printer, args=(2,))
# second = threading.Thread(target=printer, args=(5,), daemon=True)
# first.start()
# second.start()

# first.join()
# # second.join()

# end = time.time()
# print(end - start)






# import time
# import threading

# run = True
# def printer(text):
#     counter = 0
#     while run:
#         time.sleep(1)
#         counter += 1
#         print(f"\n{text}: {counter}")


# threads = []

# for i in range(11):
#     process = threading.Thread(target=printer, args=(f"Process {i}",))
#     threads.append(process)
#     process.start()

# for thread in threads:
#     thread.join()

# input("Hit Enter!")
# run = False





# import time
# import concurrent.futures

# def printer(text):
#     time.sleep(1)
#     return f"Finished {text}"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     p1 = executor.submit(printer, "Process1")
#     p2 = executor.submit(printer, "Process2")

#     print(p1.result())
#     print(p2.result())



# import time
# import concurrent.futures

# def printer(text):
#     time.sleep(1)
#     return f"Finished {text}"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     processes = [executor.submit(printer, f"Process {i}") for i in range(11)]
    

#     for process in concurrent.futures.as_completed(processes):
#         print(process.result())





# import time
# import concurrent.futures

# def printer(text):
#     time.sleep(1)
#     return f"Finished {text}"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     names = ["Process 100", "Process 55", "Process 5", "Process 1"]
#     processes = executor.map(printer, names)
    
#     for result in processes:
#         print(result)



# import time
# import concurrent.futures
# import requests

# img_urls = [
#     'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#     'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#     'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#     'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#     'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#     'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#     'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#     'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#     'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#     'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#     'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#     'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#     'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#     'https://images.unsplash.com/photo-1550439062-609e1531270e',
#     'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]

# def download(url):
#     img_data = requests.get(url).content
#     img_name = url.split("/")[3]
#     img_name = f"{img_name}.jpg"

#     with open(img_name, "wb") as image_file:
#         image_file.write(img_data)
#         print(f"{img_name} Download Completed!")


# start = time.time()
# #Total Time: 17.797471284866333
# # for url in img_urls:
# #     download(url)

# #Total Time: 13.900304794311523
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download, img_urls)


# end = time.time()
# print(f"Total Time: {end-start}")




