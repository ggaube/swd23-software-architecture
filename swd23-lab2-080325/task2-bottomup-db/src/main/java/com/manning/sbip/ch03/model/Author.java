package com.manning.sbip.ch03.model;

import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity(name = "AUTHOR")
@Table(name="AUTHORS")
public class Author {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
    private String bio;

    @ManyToMany
    @JoinTable(name = "authors_courses",
            joinColumns = {@JoinColumn(name="author_id", referencedColumnName = "id", nullable = true, updatable = true)},
            inverseJoinColumns = {@JoinColumn(name="course_id", referencedColumnName = "id", nullable = true, updatable = true)}
    )
    private Set<Course> courses = new HashSet<>();

    public Author() {}

    public Author(String name, String bio) {
        this.name = name;
        this.bio = bio;
    }

    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getBio() {
        return bio;
    }

    public Set<Course> getCourses() {
        return courses;
    }

    @Override
    public String toString() {
        return "Author{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", bio='" + bio + '\'' +
                '}';
    }
}
