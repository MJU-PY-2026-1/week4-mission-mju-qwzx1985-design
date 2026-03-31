# 파일이름 :main.py
# 작 성 자 :60222032 박성현
bucket_list = []
food1 = input("맛집 리스트 입력: ")
bucket_list.append(food1)

food2 = input("맛집 리스트 입력: ")
bucket_list.append(food2)

food3 = input("맛집 리스트 입력: ")
bucket_list.append(food3)

print(f'리스트: {bucket_list}')

vip_food = input("맛집 리스트 추가:")
bucket_list.insert(0,vip_food)
print(f"리스트: {bucket_list}")

visit_food = input("도장 깨기: ")
bucket_list.remove(visit_food)

print(f"리스트 : {bucket_list}")


