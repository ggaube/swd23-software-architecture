package database_update_event;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class RabbitmqEventDrivenApp {

    public static void main(String[] args) {
        SpringApplication.run(RabbitmqEventDrivenApp.class, args);
    }
}
