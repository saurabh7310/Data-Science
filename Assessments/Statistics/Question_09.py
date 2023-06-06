import scipy.stats as stats

# Data
data = {
    'Karan': [85, 90, 92],
    'Deepa': [70, 80, 85],
    'Karthik': [90, 85, 88],
    'Chandan': [75, 70, 75],
    'Jeevan': [95, 92, 96]
}

# Perform ANOVA
f_statistic, p_value = stats.f_oneway(*data.values())

# Print results
print("F-Statistic:", f_statistic)
print("p-value:", p_value)


# Calculate mean scores
mean_scores = {student: sum(scores) / len(scores) for student, scores in data.items()}

# Find student with highest mean score
highest_score_student = max(mean_scores, key=mean_scores.get)

# Print student with highest score
print("Student with the highest score:", highest_score_student)
