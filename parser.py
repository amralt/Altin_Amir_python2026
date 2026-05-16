import pandas as pd


hw_01_df = pd.read_csv('python-2025 - big-hw-01.csv')
hw_02_df = pd.read_csv('python-2025 - big-hw-02.csv')

def get_df_by_hw_name(hw_name: str) -> pd.DataFrame:
    if hw_name == 'hw-01':
        return hw_01_df
    elif hw_name == 'hw-02':
        return hw_02_df
    else:
        raise ValueError(f"Unknown homework name: {hw_name}")

def get_names() -> list[str]:
    names_1 = hw_01_df['Unnamed: 0'].tolist()
    names_2 = hw_02_df['Unnamed: 0'].tolist()
    names = set(names_1) | set(names_2)
    return list(names)


def get_group_names(group_id: int) -> list[str]:
    names = set()
    for tup in hw_01_df.itertuples():
        if int(tup[2]) == group_id:
            names.add(tup[1])

    for tup in hw_02_df.itertuples():
        if int(tup[2]) == group_id:
            names.add(tup[1])

    return list(names)


def get_mean_score_of_hw(hw_name: str) -> float:
    df = get_df_by_hw_name(hw_name)
    count = len(df)
    sum_scores = df['Баллы'].sum()

    mean_score = sum_scores / count
    return mean_score


def get_mean_score_of_hw_in_group(hw_name: str, group_id: int) -> float:
    df = get_df_by_hw_name(hw_name)
    sum = 0
    count = 0

    for tup in df.itertuples():
        if int(tup[2]) == group_id:
            count += 1
            sum += int(tup[4])        
    
    if count == 0:
        return 0.0

    return sum / count


def get_student_mark(student_name: str) -> int:
    student_1 = hw_01_df[hw_01_df['Unnamed: 0'] == student_name]
    student_2 = hw_02_df[hw_02_df['Unnamed: 0'] == student_name]
    
    sum_scores = 0
    if not student_1.empty:
        sum_scores += student_1['Баллы'].iloc[0]
    if not student_2.empty:
        sum_scores += student_2['Баллы'].iloc[0]

    print(sum_scores)
    if sum_scores < 1:
        return 2
    elif 1 < sum_scores < 50:
        return 3
    elif sum_scores < 80:
        return 4
    return 5


def get_mean_group_mark(group_id: int) -> float:
    sum_marks = 0
    count = 0

    for student_name in get_group_names(group_id):
        sum_marks += get_student_mark(student_name)
        count += 1
     
    if count == 0:
        return 0.0
    return sum_marks / count


if __name__ == '__main__':
    print(get_mean_group_mark(24137))

        
