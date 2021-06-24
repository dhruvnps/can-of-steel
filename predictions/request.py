import cdsapi
c = cdsapi.Client()
c.retrieve(
    'cams-europe-air-quality-forecasts',
    {
        'variable': [
            'carbon_monoxide', 'dust', 'nitrogen_dioxide', 'sulphur_dioxide', 'ozone'
        ],
        'model': 'ensemble',
        'level': [
            '0', '1000', '2000', '250', '3000', '50', '500', '5000',
        ],
        'date': '2021-01-30/2021-02-01',
        'type': 'analysis',
        'time': [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
        ],
        'leadtime_hour': '0',
        'area': [
            51.72, -0.56, 51.22, 0.35,
        ],
        'format': 'netcdf',
    },
    'download.nc')
