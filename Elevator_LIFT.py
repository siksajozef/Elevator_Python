def scan (arr,position,direction):
    seek_count=0
    distance=0
    cur_track=0
    down=[]
    up=[]
    seek_sequence=[]

    if (direction=="down"):
        down.append(0)
    if (direction=="up"):
        up.append(build_floors-1)

    for i in range(num_req_floors):
        if (arr[i]<position):
            down.append(arr[i])
        if (arr[i]>position):
            up.append(arr[i])

    print(down)
    print(up)

    down.sort()
    up.sort()

    print(down)
    print(up)

    run=2
    while run!=0:
        if (direction=="down"):
            for i in range(len(down))[::-1]:
                cur_track=down[i]
                seek_sequence.append(cur_track)
                distance=abs(cur_track-position)
                seek_count+=distance
                position=cur_track
            direction="up"

        elif(direction=="up"):
            for i in range(len(up)):
                cur_track = up[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - position)
                seek_count += distance
                position = cur_track
            direction = "down"
        run -= 1


    print("Total number of seek operations=",seek_count)
    print("Seek Sequence is:")
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

num_req_floors=int(input("Number of requested floors="))
build_floors=int(input("Number of the floors in the building="))
arr=[int(input("Requested floor=")) for i in range(num_req_floors)]
position=int(input("Position of the elevator (floor)="))
direction=(input("Direction of the elevator="))

scan(arr,position,direction)
