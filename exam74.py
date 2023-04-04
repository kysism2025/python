students = [
    {"name":"윤인성","korean":87,"math":100,"english":67,"science":95},
    {"name":"연하진","korean":89,"math":87,"english":80,"science":70},
    {"name":"나지연","korean":90,"math":65,"english":97,"science":92},
    {"name":"나선주","korean":88,"math":100,"english":44,"science":88},
    {"name":"윤이린","korean":78,"math":43,"english":33,"science":90},
    {"name":"윤명월","korean":90,"math":80,"english":60,"science":85}
]

print("이름","총점","평균", sep="\t")

for st in students:
    sum = int(st["korean"]) + int(st["math"]) + int(st["english"]) + int(st["science"])
    print(st["name"], sum, round(sum/len(students),1), sep="\t")

