import os
import django

# Вкажи шлях до твого settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab3.settings")
django.setup()

from main.repositories.repomanager import RepositoryManager


def main():
    repo = RepositoryManager()

    print("Додавання нового пасажира")
    passenger1 = repo.passengers.create(
        first_name="Ivan",
        last_name="Ivanov",
        passport="AB123456",
        is_student=True
    )

    print(f"Додано пасажира: {passenger1}")

    passenger2 = repo.passengers.create(
        first_name="Sergiy",
        last_name="Sergiiv",
        passport="AB123454",
        is_student=True
    )


    train = repo.trains.create(
        train_number="123A",
        begin_point="Kyiv",
        end_point="Lviv"
    )
    print(f"Додано поїзд: {train}")

    ticket = repo.tickets.create(
        passenger=passenger1,
        train=train,
        ticket_type="KP",
        price=500
    )
    print(f"Додано квиток: {ticket}")

    print(f"Квиток з обліком знижки: {ticket} → {ticket.price} грн")

    print("Вичитка всіх пасажирів")
    for p in repo.passengers.get_all():
        print(p)

    print("Пошук пасажира по ID")
    p_by_id = repo.passengers.get_by_id(passenger1.id)
    print(p_by_id)

    print("Оновлення пасажира")
    updated_passenger = repo.passengers.update(passenger1.id, first_name="Petro")
    print(f"Оновлений пасажир: {updated_passenger}")

    print("Видалення пасажира")
    repo.passengers.delete(passenger1.id)
    print(f"Пасажир з ID={passenger1.id} видалений")

    print("\n=== READ: Всі пасажири після видалення ===")
    for p in repo.passengers.get_all():
        print(p)

if __name__ == "__main__":
    main()


