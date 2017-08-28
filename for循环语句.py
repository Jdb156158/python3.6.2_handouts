sites = ["Jason", "Jason1","Jason2","Jason3"]
for site in sites:
    if site == "Jason2":
        print("hi,Jason2")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
