import os


def main():
    api_key = os.environ.get('weather_forecast_Api_Key')
    return api_key


if __name__=='__main__':
    main()