
def one(lines):
    # lines = '2333133121414131402'
    def generate(lines):
        id_c = 0
        disk = []
        for idx in range(len(lines)):
            if idx % 2 == 0:
                for i in range(0, int(lines[idx])):
                   disk.append(id_c)
                id_c += 1
            else:
                for i in range(0, int(lines[idx])):
                    disk.append('.')
        return disk


    def arrange(disk):
        p1 = 0
        p2 = len(disk)-1
        while p1 < p2:
            while disk[p1] != '.':
                p1 += 1
            while disk[p2] == '.':
                p2 -= 1
            disk[p1] = disk[p2]
            disk[p2] = '.'
            p1 += 1
            p2 -= 1
        return disk

    def checksum(disk):
        s = 0
        for i in range(len(disk)):
            if disk[i] == '.':
                return s
            else:
                s += disk[i] * i


    disk = generate(lines)
    disk = arrange(disk)
    return checksum(disk)






def two(lines):

    #lines = '2333133121414131402'

    def generate_disk(lines):
        id_c = 0
        disk = []
        for idx in range(len(lines)):
            if idx % 2 == 0:
                for i in range(0, int(lines[idx])):
                   disk.append(id_c)
                id_c += 1
            else:
                for i in range(0, int(lines[idx])):
                    disk.append('.')
        return disk
    def generate(disk):
        id_c = 0
        disk_t = []
        idx = 0
        curr = disk[0]
        c = 0
        while idx < len(disk):
            while idx < len(disk) and disk[idx] == curr:
                c += 1
                idx += 1

            if idx >= len(disk):
                disk_t.append([id_c, c, idx - 1])
                break

            if disk[idx] != curr:
                if curr != '.':
                    disk_t.append([id_c, c, idx - 1])
                    id_c += 1
                c = 1
                curr = disk[idx]

            idx += 1
        return disk_t


    def find_gaps(disk):
        gaps = []
        idx = 0
        while idx < len(disk):
            if disk[idx] == '.':
                start = idx
                while disk[idx] == '.':
                    idx += 1
                gaps.append([idx-start, idx-1])
            else:
                idx += 1
        return gaps


    def arrange(disk_tuple, gaps):
        p1 = 0
        s = 0
        while p1 < len(gaps):
            p2 = len(disk_tuple) - 1
            while p2 >= 0:
                if gaps[p1][0] >= disk_tuple[p2][1] and gaps[p1][1] < disk_tuple[p2][2]:

                    d = disk_tuple[p2]
                    d = [d[0], d[1], gaps[p1][1] - gaps[p1][0] + d[1]]
                    s += calc_one_disk_checksum(d)
                    gaps[p1][0] = gaps[p1][0] - disk_tuple[p2][1]
                    del disk_tuple[p2]
                    p2 -= 1
                    if gaps[p1][0] > 0:
                        continue
                    break
                else:
                    p2 -= 1
            p1 += 1
        s += unmoved(disk_tuple)
        return s

    def calc_one_disk_checksum(dt):
        idx, length, end_pos = dt
        s = 0
        for i in range(length):
            s += (idx * (end_pos - i))
        return s
    def unmoved(disk_tuple):
        s = 0
        for i in disk_tuple:
            s += calc_one_disk_checksum(i)
        return s





    disk = generate_disk(lines)
    disk_tuple = generate(disk)
    gaps = find_gaps(disk)
    return arrange(disk_tuple, gaps)





