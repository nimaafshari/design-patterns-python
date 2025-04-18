from multi_threaded_singleton import Singleton
import threading


def main():
    # Create multiple threads to test the Singleton implementation
    threads = []
    instances = []

    def get_instance():
        instance = Singleton()
        instances.append(instance)

    for i in range(5):
        thread = threading.Thread(target=get_instance)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Verify that all threads received the same instance
    assert all(
        instance is instances[0] for instance in instances
    ), "Singleton instances are not the same!"


if __name__ == "__main__":
    main()
    print("All threads received the same Singleton instance.")
