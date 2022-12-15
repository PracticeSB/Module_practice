#Test module.py 파일
PI = 3.14592

def number_input():
    output = input("숫자 입력>")
    return float(output)

def get_circumference(radius):
    return 2*PI*radius

def get_circle_area(radius):
    return PI*radius*radius

if __name__ == "__main__":
    print('이게 메인 루프입니다!')
