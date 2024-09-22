# ECS506-Group3 FDM Expenses Application

## Members
- Aivaras Barcys (a.barcys@se22.qmul.ac.uk)
- Armin Shahnami (a.shahnami@se22.qmul.ac.uk)
- Ayotunde Ogunnaiya (a.ogunnaiya@se22.qmul.ac.uk)
- Chee-Ho Nim (c.nim@se22.qmul.ac.uk)
- Konrad Vincler (k.d.vincler@se22.qmul.ac.uk)
- Mohamed Ait-Hocine (m.ait-hocine@se22.qmul.ac.uk)
- Sefa Yildirim (s.a.yildirim@se22.qmul.ac.uk)

## Getting Started

### Backend

#### Installation

Install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

#### Usage

Enter your PostgreSQL database URI in a .env file in the following format:

```env
DATABASE_URI=postgresql+psycopg://user:password@host:port/database_name
```

Run the following to start the backend server:

```bash
flask run
```

Use the ```--debug``` flag for debugging mode.

### Frontend

Install the dependencies by running the following command:

```bash
npm install
```

Run the following to start the application:
```bash
npm run
```
