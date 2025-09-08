from report_generator import generate_summary

results = {
    "best_promo": "Promotion 1",
    "means": {"1": 58.08, "2": 47.36, "3": 55.37},
    "intervals": {
        "1": [55.65, 60.69],
        "2": [45.29, 49.57],
        "3": [52.95, 57.82]
    }
}

generate_summary(results)
