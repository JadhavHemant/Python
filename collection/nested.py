states=[
    {"state_id":1,"state_name":"maharashtra","cities":[
        {"city_id":1,"city_name":"mumbai"},
        {"city_id":2,"city_name":"pune"}
    ]},
    {"state_id":2,"state_name":"gujrat","cities":[
        {"city_id":3,"city_name":"ahmdabad"},
         {"city_id":4,"city_name":"surat"}
    ]}
 ]
for s in states:
    print(str(s["state_id"])+" "+s["state_name"])
    for c in s["cities"]:
        print("\t"+str(c["city_id"])+" "+c["city_name"])
    print("----------------------------")



    