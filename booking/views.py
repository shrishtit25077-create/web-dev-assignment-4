from django.shortcuts import render


def home(request):
    train = {
        'train_no': '12952',
        'train_name': 'Delhi Rajdhani Express',
        'source': 'New Delhi',
        'destination': 'Mumbai Central',
        'departure': '16:55',
        'arrival': '08:35',
    }
    return render(request, 'booking/home.html', {'train': train})


def train_search(request):
    trains = [
        {
            'train_no': '12952',
            'train_name': 'Delhi Rajdhani Express',
            'source': 'New Delhi',
            'destination': 'Mumbai Central',
            'departure': '16:55',
            'arrival': '08:35',
        },
        {
            'train_no': '12001',
            'train_name': 'Bhopal Shatabdi Express',
            'source': 'Bhopal',
            'destination': 'New Delhi',
            'departure': '06:00',
            'arrival': '14:00',
        },
        {
            'train_no': '12302',
            'train_name': 'Howrah Rajdhani Express',
            'source': 'Howrah',
            'destination': 'New Delhi',
            'departure': '16:55',
            'arrival': '10:00',
        },
    ]
    return render(request, 'booking/train_search.html', {'trains': trains})


def passenger_details(request):
    passenger = {
        'name': 'Devishi',
        'age': 18,
        'gender': 'Female',
        'coach': 'B2',
        'berth': 'Lower',
    }
    return render(request, 'booking/passenger_details.html', {'passenger': passenger})


def booking_confirmation(request):
    booking = {
        'passenger_name': 'Devishi',
        'train_no': '12952',
        'train_name': 'Delhi Rajdhani Express',
        'source': 'New Delhi',
        'destination': 'Mumbai Central',
        'coach': 'B2',
        'berth': 'Lower',
    }
    return render(request, 'booking/confirmation.html', {'booking': booking})
