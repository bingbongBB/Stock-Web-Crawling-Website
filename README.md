# Stock-Web-Crawling-Website
# Taiwan Stock Market Query Website

A stock market query website developed using Django framework, providing historical data and real-time stock quotes for Taiwan Stock Exchange.

## Features

- Historical stock data query
- Real-time stock quote lookup
- Trend charts and candlestick charts visualization
- Basic stock information display

## Technical Architecture

- Frontend: HTML, CSS, JavaScript
- Backend: Django Framework
- Database: SQLite3
- Third-party packages:
  - twstock: Taiwan stock data crawler
  - pandas: Data processing
  - matplotlib: Chart rendering

## Installation

1. Create virtual environment:
```bash
virtualenv venv1
```
2. Activate virtual environment:
```bash
venv1\Scripts\activate
```
3. Install required packages:
```bash
pip install django twstock pandas matplotlib
```
4. Create Django project:
```bash
django-admin startproject [project_name]
```
5. Create app:
```bash
python manage.py startapp [app_name]
```

## Usage Guide

1. Historical Data Query:
   - Input stock code, year, and month
   - System displays trading data and trend charts for the specified time period

2. Real-time Data Query:
   - Input stock code
   - Displays real-time stock price, high/low prices, trading volume, and other information

## System Requirements

- Python 3.7+
- Django 3.0+
- Internet connection (for real-time data query)
