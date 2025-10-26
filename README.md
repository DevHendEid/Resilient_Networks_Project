Resilient_Networks_Project/
│
├── data/                     ← ملفات الشبكات (الخام)
│   ├── za_16464_core_max.graphml.gz     # ZeroAccess
│   └── roadNet-CA.txt.gz                # road network
│
├── src/                      ← كود بايثون المنظم
│   ├── __init__.py
│   ├── load_graphs.py         # تحميل وقراءة الشبكات
│   ├── metrics.py             # حساب المقاييس العامة
│   ├── robustness.py          # محاكاة الهجمات
│   ├── plots.py               # الرسوم البيانية (degree, robustness)
│   └── main.py                # الملف الرئيسي للتشغيل
│
├── results/                  ← نتائج المشروع
│   ├── figures/               # صور الرسوم (png/pdf)
│   ├── metrics_summary.csv    # جدول المقاييس
│   └── robustness_curves.csv  # منحنيات الصمود
│
├── report/                   ← مجلد التقرير النهائي
│   └── Resilient_Networks_Report.pdf
│
├── requirements.txt           ← المكتبات المطلوبة
└── README.md                  ← وصف المشروع وطريقة التشغيل
# Resilient Networks Project (Winter Term 2024/2025)

## Overview
Analysis of network resilience using two real-world graphs:
1. ZeroAccess P2P Botnet (GitHub: iBigQ/botnet-graphs)
2. California Road Network (SNAP)

## Objectives
- Compute ≥5 network metrics (density, clustering, path length, assortativity, etc.)
- Analyze robustness under random and targeted attacks
- Compare structural differences between a botnet and a road network

## Run
