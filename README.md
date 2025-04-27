# First Streamlit App 🚀

> **DADS5001 - First Web Application with Streamlit**

โปรเจกต์นี้คือแอปพลิเคชันตัวแรกที่พัฒนาด้วย [Streamlit](https://streamlit.io/)!
เน้นการเรียนรู้การสร้าง Web Application แบบโต้ตอบได้ (Interactive Web App) ด้วยภาษา Python โดยใช้ ข้อมูลการเรียกรถ Uber ในเมืองนิวยอร์ก (NYC) เป็นตัวอย่างจริงในการนำเสนอข้อมูล

## Uber Pickups in NYC 🚕📊

ในโปรเจกต์นี้ เรานำข้อมูลจริงจาก [Uber pickups dataset](https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz) — ซึ่งเป็นข้อมูลการเรียกรถ Uber ในเดือนกันยายน 2014 — มาวิเคราะห์และแสดงผลผ่านแอปแบบอินเทอร์แอคทีฟ เพื่อให้ผู้ใช้งานสามารถสำรวจข้อมูลได้ด้วยตัวเอง ผ่านแผนที่ กราฟ และตัวเลือกต่าง ๆ

## 🌟 Features

- **แสดงข้อมูลดิบ (Raw Data)**: ผู้ใช้สามารถเลือกดูข้อมูลการเรียกรถทั้งหมดได้
- **กราฟแท่ง (Bar Chart)**: วิเคราะห์จำนวนการเรียกรถแยกตามชั่วโมงในแต่ละวัน
- **แผนที่ 2D และ 3D**:
  - แผนที่ 2D: แสดงตำแหน่งการเรียกรถในแต่ละชั่วโมง
  - แผนที่ 3D: เพื่อแสดงความหนาแน่นของจุดเรียกรถ
- **การเลือกช่วงวันที่ (Date Range)**: ผู้ใช้สามารถกรองข้อมูลตามช่วงวันที่ที่ต้องการ
- **กราฟเส้น (Line Chart)**: แสดงจำนวนการเรียกรถในแต่ละวันด้วย Plotly
- **ปุ่มโต้ตอบ (Interactive Button)**: เพิ่มตัวนับจำนวนครั้งที่กดปุ่ม
- **Select Box**: ให้ผู้ใช้เลือกตัวเลือกที่ต้องการ

## 📊 Data Source

ข้อมูลทั้งหมดนำมาจากชุดข้อมูล Uber rides เดือนกันยายน 2014 ซึ่งเผยแพร่โดย Streamlit เพื่อใช้ในการสาธิต ([Uber pickups dataset](https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz))

ข้อมูลนี้ประกอบด้วยรายละเอียดเช่น:

- วันที่และเวลาที่มีการเรียกรถ
- พิกัดตำแหน่ง (Latitude, Longitude) ของผู้โดยสาร
- จำนวนการเรียกรถในแต่ละช่วงเวลา

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

---
