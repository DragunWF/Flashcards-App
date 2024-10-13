import sys
import os

# Enables the helpers modules to be imported
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
)
from helpers.flashcard import Flashcard

TEST_101 = {
    "topic": "Computer Programming",
    "flashcards": [
        Flashcard("Object-Oriented Programming (OOP)",
                  "A programming paradigm that organizes code using objects, which contain data and methods."),
        Flashcard("Linked List", "A data structure consisting of nodes, where each node contains a value and a reference to the next node."),
        Flashcard(
            "Pointer", "A variable in programming that holds a reference to an object, not the actual object itself."),
        Flashcard(
            "Recursion", "A function that calls itself in order to solve smaller instances of the same problem."),
        Flashcard(
            "Compilation", "The process of converting high-level programming code into machine-readable code."),
        Flashcard(
            "Polymorphism", "The ability of a programming language to present the same interface for different data types."),
        Flashcard("Encapsulation",
                  "The concept of restricting access to certain parts of an object and bundling data with methods."),
        Flashcard(
            "Algorithm", "A step-by-step procedure or formula for solving a problem."),
        Flashcard("Big O Notation",
                  "A mathematical notation to describe the performance or complexity of an algorithm."),
        Flashcard("Lambda Function",
                  "A small anonymous function defined using the lambda keyword.")
    ]
}

TEST_102 = {
    "topic": "Data Structures",
    "flashcards": [
        Flashcard(
            "Array", "A data structure used to store multiple values in a single variable."),
        Flashcard("Binary Search Tree",
                  "A tree data structure where each node has at most two children, left and right."),
        Flashcard(
            "Hash Table", "A data structure that stores data in an associative manner using key-value pairs."),
        Flashcard(
            "Stack", "A linear data structure that follows the LIFO (Last In First Out) principle."),
        Flashcard(
            "Queue", "A linear data structure that follows the FIFO (First In First Out) principle."),
        Flashcard(
            "Graph", "A data structure used to represent relationships in the form of nodes and edges."),
        Flashcard(
            "Set", "A collection of unique elements without any particular order."),
        Flashcard(
            "Heap", "A specialized tree-based data structure that satisfies the heap property."),
        Flashcard(
            "Trie", "A tree-like data structure used for storing strings, especially for fast prefix-based searches."),
        Flashcard(
            "Deque", "A double-ended queue where elements can be added or removed from both ends.")
    ]
}

TEST_103 = {
    "topic": "Networking",
    "flashcards": [
        Flashcard("IP Address",
                  "A unique address that identifies a device on a network."),
        Flashcard(
            "DNS", "A system that translates domain names into IP addresses."),
        Flashcard(
            "HTTP", "A protocol used for transmitting hypermedia documents, such as HTML."),
        Flashcard("Socket Programming",
                  "A way to communicate between two devices over a network."),
        Flashcard(
            "Firewall", "A network security system that monitors and controls incoming and outgoing traffic."),
        Flashcard(
            "VPN", "A secure connection over the internet between a device and a network."),
        Flashcard(
            "TCP/IP", "A suite of protocols used for communication on the internet."),
        Flashcard(
            "Ping", "A utility used to test the reachability of a host on an IP network."),
        Flashcard(
            "MAC Address", "A unique identifier assigned to a network interface controller."),
        Flashcard("Load Balancer",
                  "A device that distributes network or application traffic across multiple servers.")
    ]
}

TEST_104 = {
    "topic": "Cybersecurity",
    "flashcards": [
        Flashcard(
            "Encryption", "The process of converting data into a secret code to prevent unauthorized access."),
        Flashcard(
            "Firewall", "A system designed to block unauthorized access while permitting authorized communication."),
        Flashcard(
            "Malware", "Software specifically designed to disrupt, damage, or gain unauthorized access to systems."),
        Flashcard(
            "Phishing", "A method of fraudulently obtaining sensitive information by pretending to be a trustworthy entity."),
        Flashcard("Zero-Day Exploit",
                  "An attack that occurs before the vulnerability is known to the software developer."),
        Flashcard("Brute Force Attack",
                  "An attempt to guess a password or encryption key through trial and error."),
        Flashcard(
            "Ransomware", "A type of malware that locks users out of their data and demands a ransom to unlock it."),
        Flashcard("Social Engineering",
                  "The use of deception to manipulate individuals into divulging confidential information."),
        Flashcard("Two-Factor Authentication",
                  "An extra layer of security requiring not only a password but also a second factor."),
        Flashcard("Public Key Infrastructure (PKI)",
                  "A system used to create, manage, and distribute digital certificates.")
    ]
}

TEST_105 = {
    "topic": "Software Development",
    "flashcards": [
        Flashcard("Agile Methodology",
                  "An iterative approach to software development focusing on collaboration and flexibility."),
        Flashcard("Version Control",
                  "A system used to manage changes to software over time."),
        Flashcard(
            "CI/CD", "Continuous Integration and Continuous Deployment for automating software delivery."),
        Flashcard(
            "Unit Testing", "Testing individual components of software to ensure they work as expected."),
        Flashcard(
            "Code Review", "The process of systematically examining source code for errors and improvements."),
        Flashcard("Design Patterns",
                  "Reusable solutions to common software design problems."),
        Flashcard(
            "DevOps", "A set of practices that combines software development and IT operations."),
        Flashcard(
            "API", "A set of protocols for building and interacting with software applications."),
        Flashcard("Microservices",
                  "A software architecture style where applications are composed of loosely coupled services."),
        Flashcard("Technical Debt",
                  "The cost of additional rework caused by choosing an easy solution now instead of a better one.")
    ]
}
