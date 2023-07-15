def read(t,a,b,z):
    display_list = []

    with open (t + z + ".txt", "r") as data_file:
        for line in data_file:
            display_list.append(line.strip().split(','))
    return display_list[a][b]

def total(aa,bb,cc,dd,ee):
    tot = []
    num = []    
    num = int(aa) + int(bb) + int(cc) + int(dd) + int(ee) - 200
    oth = int(1)

    with open ("total.txt", "r") as data_file:
        for line in data_file:
            tot.append(line.strip().split(','))
    return tot [num][oth]

def subtest(raw, row, col):
    mean = []
    sd = []

    cn = col + 1

    with open ("subtst.txt", "r") as data_file:
        for line in data_file:
            mean.append(line.strip().split(','))
        mean = mean [row][col]
        
    with open ("subtst.txt", "r") as data_file:
        for line in data_file:
            sd.append(line.strip().split(','))
        sd = sd [row][cn]
        
    t = round((float(raw) - float(mean))/float(sd)*10 + 50)
    return int(t)
        
name = input('Name :')
age = input('Age :')

ll = int(input('List Learning: '))
sm = int(input('Story Memory: '))
fc = int(input('Figure Copy: '))
lo = int(input('Line Orientation: '))
pn = int(input('Picture Naming: '))
sf = int(input('Semantic Fluency: '))
ds = int(input('Digit Span: '))
cd = int(input('Coding: '))
lr = int(input('List Recall: '))
lg = int(input('List Recognition: '))
sr = int(input('Story Recall: '))
fr = int(input('Figure Recall: '))

if age <= '39':
    ager = '20'
    aget = 0
elif age <= '49':
    ager = '40'
    aget = 2
elif age <= '59':
    ager = '50'
    aget = 4
elif age <= '69':
    ager = '60'
    aget = 6
elif age <= '79':
    ager = '70'
    aget = 8
else:
    ager = '80'
    aget = 10

imi = read('im', ll, sm, ager)
vci = read('vc',fc, lo, ager)
lni = read('ln', sf, pn, ager)
ati = read('at', cd, ds, ager)
cm = int(lr) + int(sr) + int(fr)
dmi = read('dm', cm, lg, ager)
tti = total(imi, vci, lni, ati, dmi) 
llt = subtest(ll, 0, aget)
smt = subtest(sm, 1, aget)
fct = subtest(fc, 2, aget)
lot = subtest(lo, 3, aget)
pnt = subtest(pn, 4, aget)
sft = subtest(sf, 5, aget)
dst = subtest(ds, 6, aget)
cdt = subtest(cd, 7, aget)
lrt = subtest(lr, 8, aget)
lgt = subtest(lg, 9, aget)
srt = subtest(sr, 10, aget)
frt = subtest(fr, 11, aget)

print( "         ** RBANS **")
print( " ")
print( "Index Scores (Scaled scores):")
print( "Immediate Memory:            ",imi)
print( "Visuospatial/Constructional: ",vci)
print( "Language:                    ",lni)
print( "Attention:                   ",ati)
print( "Delayed Memory:              ",dmi)
print( "Total Score:                 ",tti)
print( " ")
print( "Subtest Scores (T-scores):")
print( "List Learning:               ",llt)
print( "Story Memory:                ",smt)
print( "Figure Copy:                 ",fct)
print( "Line Orientation:            ",lot)
print( "Picture Naming:              ",pnt)
print( "Semantic Fluency:            ",sft) 
print( "Digit Span:                  ",dst)
print( "Coding:                      ",cdt)
print( "List Recall:                 ",lrt)
print( "List Recognition:            ",lgt)
print( "Story Recall:                ",srt)
print( "Figure Recall:               ",frt)

