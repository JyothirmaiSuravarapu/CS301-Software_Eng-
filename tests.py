# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from ticketing.models import Event, Ticket

class TicketingIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.event = Event.objects.create(
            name='Test Event',
            date='2022-04-01',
            time='10:00:00',
            venue='Test Venue'
        )

    def test_buy_ticket(self):
        response = self.client.get(reverse('buy_ticket', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)

        # Simulate form submission
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'quantity': 2
        }
        response = self.client.post(reverse('buy_ticket', args=[self.event.id]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ticket_success'))

        # Check that the ticket was created
        tickets = Ticket.objects.filter(event=self.event, email='testuser@example.com')
        self.assertEqual(len(tickets), 2)