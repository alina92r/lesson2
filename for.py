students_scores = [
    {'school_class': '4a', 'scores': [5,4,4,5,2]}, 
    {'school_class': '4б', 'scores': [5,5,4,5,2,4,3]},
    {'school_class': '5a', 'scores': [5,3,2,2,2,5,5]},
    {'school_class': '6a', 'scores': [5,3,5,5]}
    ]



scores_school=0
count_scores=0
for school_class in students_scores:
    scores_sum=0
    for score in school_class['scores']:
        scores_sum += score
        scores_school += score
        count_scores += 1
        #print(scores_sum)
    print(f"Средний балл по классу: {scores_sum/len(school_class['scores'])}")

print(f"Средний балл по школе: {scores_school/count_scores}")
print(scores_school)
print(count_scores)