---
toc: true
comments: true
layout: post
title: Computers and Networks (Unit 4)
description: Add Definitions from Unit 4 Computer Systems and Networks
image: /images/apcsp.png
categories: []
type: ap
week: 29
---

## Requirements
> Work through College Board Unit 4... blog, add definitions, and pictures.  Be creative, for instance make a story of Computing and Networks that is related to your PBL experiences this year.


### How a Computer Works
> As we have learned, a computer needs aa program to do something smart.  The sequence of a program initiates a series of actions with the computers Central Processing Unit (CPU). This component is essentially a binary machine focussing on program instructions provided.  The CPU retrieives and stores the data it acts upon in Random Access Memory (RAM). Between the CPU, RAM, and Storage Devices a computer can work with many programs and large amounts of data.

List specification of your Computer, or Computers if working as Pair/Trio
- Processor: Intel Core i7 processor
- Memory: 16GB of RAM
- Storage: 256GB
- OS: Windows 11 Home

Define or describe usage of Computer using Computer Programs. Pictures are preferred over a lot of text.  Use your experience.

- Input device: An input device is a device that is used to input data into a computer. Examples of input 
devices include keyboards, mice, and microphones.

- Output device: An output device is a device that is used to output data from a computer. Examples of output devices include monitors, printers, and speakers.

- Program file: A program file is a file that contains instructions for a computer to follow. Program files are typically written in a programming language, such as Python or Java.

- Program code: Program code is the set of instructions that make up a program file. Program code is written in a programming language and is typically stored in a text file.

- Processes: A process is a program that is currently running on a computer. Processes are managed by the operating system and can be created, suspended, and terminated by the user.

- Ports: A port is a connection point on a computer that can be used to connect to other devices. Examples of ports include USB ports, Ethernet ports, and HDMI ports.

- Data file: A data file is a file that contains data. Data files can be used to store text, images, audio, video, and other types of data.

- Inspect running code: Inspecting running code is the process of examining the instructions that are currently being executed by a computer program. This can be done using a debugger, which is a tool that allows users to step through the instructions of a program one at a time.

- Inspect variables: Inspecting variables is the process of examining the values of variables that are currently being used by a computer program. This can be done using a debugger, which allows users to view the values of variables as they change during the execution of a program.


![Computer Hardware]({{site.baseurl}}/images/cpu.jpeg)


### The Internet
> Watch/review College Board Daily Video for 4.1.1

- Essential Knowledge
    - A computing device is a physical artifact that can run a program. Some examples include computers, tablets, servers, routers, and smart sensors.
    - A computing system is a group of computing devices and programs working together for a common purpose.
    - A computer network is a group of interconnected computing devices capable of sending or receiving data.
    - A computer network is a type of computing system. 
    - A path between two computing devices on a computer network (a sender and a receiver) is a sequence of directly connected computing devices that begins at the sender and ends at the receiver.
    - Routing is the process of finding a path from sender to receiver.
    - The bandwidth of a computer network is the maximum amount of data that can be sent in a fixed amount of time.
    - Bandwidth is usually measured in bits per second

- Complete Vocabulary Matching Activity.  Incorporate this into your learnings from year.  To analyze measure path and latency use `traceroute` and `ping` commands from Linux Terminal.  

    - Path: A path is a sequence of connected points. In computer science, a path can refer to a sequence of directories or files, or a sequence of network nodes.
    - Route: A route is a specific path between two points. In computer science, a route can refer to a specific path between two network nodes, or a specific path between two files or directories.
    - Computer system: A computer system is a collection of hardware and software that works together to perform tasks. A computer system typically includes a central processing unit (CPU), memory, storage, input/output devices, and software.
    - Computer device: A computer device is a physical object that is used to interact with a computer system. Examples of computer devices include keyboards, mice, monitors, printers, and scanners.
    - Bandwidth: Bandwidth is the amount of data that can be transmitted over a network in a given amount of time. Bandwidth is measured in bits per second (bps).
    - Computer network: A computer network is a group of computers that are connected together. Computer networks allow computers to share resources, such as files, printers, and internet access.


> Watch/review College Board Daily Video 4.1.2

- Complete True of False Questions

- True
- False
- False
- True
- True
- False
- True

- Essential Knowledge
    - The internet is a computer network consisting of interconnected networks that use standardized, open (nonproprierary) communication protocols.
    - Access to the internet depends on the ability to connect a computing device to an internet connected device.
    - A protocol is an agreed-upon set of rules that specify the behavior of a system.
    - The protocols used in the internet are open, which allows users to easily connect additional computing devices to the internet.
    - Routing on the internet is usually dynamic; it is not specified in advance
    - The scalability of a system is the capacity for the system to change in size and scale to meet new demands.
    - The internet was designed to be scalable
    - Information is passed through the internet as a data stream. Data streams contain chunks of data, which are encapsulated in packets. 
    - Packets contain a chunk of data and metadata used for routing the packet between the origin and the destination on the internet, as well as for data reassembly.
    - Packets may arrive at the destination in order, out of order, or not at all
    - IP, TCP and UDP are common protocols used on the internet.
    - The world wide web is a system of linked pages, programs, and files.
    - HTTP is a protocol used by the world wide web
    - The world wide web uses the internet

- Go over AP videos, vocabulary, and essential knowledge.  Draw a diagram showing the internet and its many levels. A preferred diagram would using your knowledge of frontend, backend, deployment, etc.  Picture would highligh vocabulary by illustration. The below illustration have some ideas

![Full Stack]({{site.baseurl}}/images/fullstack.png)

## My Canva Illustration

![Local System Computer](https://user-images.githubusercontent.com/109186517/235439636-4d8e9a64-3a79-45ef-82f8-4b1911a50eed.png)

![Internet Process Layers](https://user-images.githubusercontent.com/109186517/235528531-90e333e2-f651-4f85-81e8-7852ba54b110.png)


- Often we draw pictures of machines communicating over the Internet with arrows.  However, the real communication goes through protocol layers and the machine and then is trasported of the network.   For College Board and future Computer Knowledge you should become familiar with the following ...

```
     User Machine  <---> Frontend Server <---> Backend Server
    +-----------+         +-----------+         +-----------+
    |  Browser  |         |  GH Page  |         |   Flask   |
    +-----------+    ^    +-----------+    ^    +-----------+
    |    HTTP   |    |    |    HTTP   |    |    |    HTTP   |
    +-----------+    |    +-----------+    |    +-----------+
    |    TCP    |    |    |    TCP    |    |    |    TCP    |   
    +-----------+    |    +-----------+    |    +-----------+
    |     IP    |    V    |     IP    |    V    |     IP    |
    +-----------+         +-----------+         +-----------+
    |  Network  |  <--->  |  Network  |  <--->  |  Network  |
    +-----------+         +-----------+         +-----------+
```

The "http" layer is an application layer protocol in the TCP/IP stack, used for ***communication between web browsers and web servers***. It is the protocol used for transmitting data over the World Wide Web.

The "transport" layer (TCP) is responsible for providing reliable data transfer between applications running on different hosts.  The TCP protocol segments the data into smaller ***chunks called "segments"***. Each segment contains a sequence number that identifies its position in the original stream of data, as well as other control information such as source and destination port numbers, and checksums for error detection.

The "ip" layer is responsible for packetizing data received from the TCP layer of the protocol stack, and then ***encapsulating the data into IP packets***. The IP packets are then sent to the lower layers of the protocol stack for transmission over the network.

The "network" layer is responsible for ***routing data packets between networks*** using the Internet Protocol (IP). This layer handles tasks such as packet addressing and routing, fragmentation and reassembly, and ***network congestion*** control.


### Fault Tolerance
> Watch both Daily videos for 4.2

- Complete the network activity, summarize your understanding of fault tolerance.


### Parallel and Distributed Computing
> Review previous lecture on Parallel Computing and watch Daily vidoe 4.3.  Think of ways to make something in you team project to utilize Cores more effectively.  Here are some thoughts to add to your story of Computers and Networks...

- What is naturally Distributed in Frontend/Backend archeticture?  

In a distributed frontend/backend architecture, the frontend is split into multiple, independent components that can be developed and deployed separately. This allows for faster development, easier maintenance, and greater scalability.

- Analyze this command in Docker: ```ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8086"```.   Determine if there is options are options in this command for parallel computing within the server that runs python/gunicorn.  Here is an [article](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7)


> Last week we discussed parallel computing on local machine.  There are many options.  Here is something to get parallel computing work with a tool called Ray.
- Review this [article](https://www.anyscale.com/blog/writing-your-first-distributed-python-application-with-ray)...  Can you get parallel code on images to work more effectively?  I have not tried Ray.

Yes, there are several ways to get parallel code on images to work more effectively. One way is to divide the image into smaller blocks and process each block in parallel. Another way is to use a specialized parallel image processing library. Finally, you can also use a distributed computing platform to run your code on multiple machines.

- Code example from ChatGPT using squares.  This might be more interesting if nums we generated to be a lot bigger.

```python
import ray

# define a simple function that takes a number and returns its square
def square(x):
    return x * x

# initialize Ray
ray.init()

# create a remote function that squares a list of numbers in parallel
@ray.remote
def square_list(nums):
    return [square(num) for num in nums]

# define a list of numbers to square
nums = [1, 2, 3, 4, 5]

# split the list into two parts
split_idx = len(nums) // 2
part1, part2 = nums[:split_idx], nums[split_idx:]

# call the remote function in parallel on the two parts
part1_result = square_list.remote(part1)
part2_result = square_list.remote(part2)

# get the results and combine them
result = ray.get(part1_result) + ray.get(part2_result)

# print the result
print(result)

```
