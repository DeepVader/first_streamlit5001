# First Streamlit App 🚀

> **DADS5001**

โปรเจกต์นี้เป็นงานชิ้นแรกที่พัฒนาด้วย [Streamlit](https://streamlit.io/) เพื่อสร้าง Web Application แบบโต้ตอบได้ โดยเน้นการแสดงข้อมูลการเรียกรถ Uber ในเมืองนิวยอร์ก (NYC)

## Uber Pickups in NYC 🚕📊

โปรเจกต์นี้เป็นการสร้าง Web Application ด้วย [Streamlit](https://streamlit.io/) เพื่อแสดงข้อมูลการเรียกรถ Uber ในเมืองนิวยอร์ก (NYC) โดยมีฟีเจอร์การโต้ตอบ (Interactive) และการแสดงผลข้อมูลในรูปแบบต่าง ๆ เช่น กราฟ, แผนที่ 2D/3D และอื่น ๆ

## 🌟 Features

- **แสดงข้อมูลดิบ (Raw Data)**: ผู้ใช้สามารถเลือกดูข้อมูลดิบได้
- **กราฟแท่ง (Bar Chart)**: แสดงจำนวนการเรียกรถ Uber แยกตามชั่วโมง
- **แผนที่ 2D และ 3D**:
  - แผนที่ 2D: แสดงตำแหน่งการเรียกรถในแต่ละชั่วโมง
  - แผนที่ 3D: ใช้ PyDeck แสดงข้อมูลในรูปแบบ Hexagon Layer และ Scatterplot Layer
- **การเลือกช่วงวันที่ (Date Range)**: ผู้ใช้สามารถกรองข้อมูลตามช่วงวันที่ที่ต้องการ
- **กราฟเส้น (Line Chart)**: แสดงจำนวนการเรียกรถในแต่ละวันด้วย Plotly
- **ปุ่มโต้ตอบ (Interactive Button)**: เพิ่มตัวนับจำนวนครั้งที่กดปุ่ม
- **Select Box**: ให้ผู้ใช้เลือกตัวเลือกที่ต้องการ

## 📊 Data Source

ข้อมูลที่ใช้ในโปรเจกต์นี้มาจาก [Uber pickups dataset](https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz) ซึ่งเป็นข้อมูลการเรียกรถ Uber ในเดือนกันยายน 2014

## 🔗 Live Demo

ทดลองใช้งานแอปได้ที่นี่:

👉 [Uber Pickups App](https://firstapp5001-zspq95pjessbdbvxxmxs2w.streamlit.app/?classId=e08fcee7-1a01-4403-b7ee-3f89c558f29f&assignmentId=d17fe288-4f27-4cc9-b306-6fa968085241&submissionId=3112f7dc-e170-148d-4267-d66a46238be5)

## 📦 Dependencies

- Python 3.12+
- Streamlit 1.44.1
- Pandas 2.2.3
- NumPy 2.2.5
- PyDeck 0.9.1
- Plotly 6.0.1
