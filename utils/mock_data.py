def get_mock_data():
    data = {
        "date": 1719134667,
        "location_name": "Tehran",
        "temp": {
            "now": 30.66,  
            "min": 30.31,
            "max": 32.70
        },
        "weather": {
            "icon_type": "broken clouds"
        },
        "wind": {
            "speed": 4.12,
            "deg": 140.0
        },
        "humidity": 16,
        "pressure": 1013,
        "sunrise": 1719105575,
        "sunset": 1719158047,
        "future_hours": [
            {
                "date": 1719136800,
                "temp": 31,
                "weather": {
                    "icon_type": "broken clouds"
                }
            },
            {
                "date": 1719140400,
                "temp": 32,
                "weather": {
                    "icon_type": "broken clouds"
                }
            },
            {
                "date": 1719144000,
                "temp": 30,
                "weather": {
                    "icon_type": "light rain"
                }
            },
            {
                "date": 1719147600,
                "temp": 31,
                "weather": {
                    "icon_type": "scattered clouds"
                }
            },
            {
                "date": 1719151200,
                "temp": 32,
                "weather": {
                    "icon_type": "few clouds"
                }
            }
        ],
        "future_days": [
            {
                "date": 1719131400,
                "temp": {
                    "min": 27.50,
                    "max": 32.18
                },
                "weather": {
                    "icon_type": "light rain"
                }
            },
            {
                "date": 1719217800,
                "temp": {
                    "min": 25.07,
                    "max": 34.07
                },
                "weather": {
                    "icon_type": "moderate rain"
                }
            },
            {
                "date": 1719304200,
                "temp": {
                    "min": 27.04,
                    "max": 35.75
                },
                "weather": {
                    "icon_type": "light rain"
                }
            },
            {
                "date": 1719390600,
                "temp": {
                    "min": 28.73,
                    "max": 34.16
                },
                "weather": {
                    "icon_type": "sky is clear"
                }
            },
            {
                "date": 1719477000,
                "temp": {
                    "min": 28.62,
                    "max": 34.96
                },
                "weather": {
                    "icon_type": "light rain"
                }
            }
        ]
    }
    return data