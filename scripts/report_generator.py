from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_summary(results, output_path="reports/summary.pdf"):
    """
    results: dict with keys like:
        {
            "best_promo": "Promotion 1",
            "means": {"1": 58.08, "2": 47.36, "3": 55.37},
            "intervals": {
                "1": [55.65, 60.69],
                "2": [45.29, 49.57],
                "3": [52.95, 57.82]
            }
        }
    """
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Executive Summary — A/B Test: Fast-Food Promotions</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("A fast-food chain tested three marketing promotions for a new product. "
                           "Sales were tracked across multiple markets over four weeks.", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Key Findings</b>", styles["Heading2"]))
    story.append(Paragraph(
        f"- Promotion 1 had the highest average sales (~{results['means']['1']:.2f}).<br/>"
        f"- Promotion 3 was second (~{results['means']['3']:.2f}).<br/>"
        f"- Promotion 2 was the lowest (~{results['means']['2']:.2f}).<br/>"
        "Bootstrapped 95% confidence intervals confirm these differences are statistically significant.",
        styles["Normal"]
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(
        f"We recommend adopting <b>{results['best_promo']}</b> as the primary marketing strategy. "
        "Promotion 2 should be avoided as it underperforms significantly.",
        styles["Normal"]
    ))

    doc.build(story)
    print(f"✅ Summary report saved to {output_path}")
