package event_driven_two_queues;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class RabbitMqEventDrivenApp {

    public static void main(String[] args) {
        SpringApplication.run(RabbitMqEventDrivenApp.class, args);
    }
}

