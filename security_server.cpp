#include <iostream>
#include <winsock2.h>
#include <string>

#pragma comment(lib, "ws2_32.lib") // Link the networking library

std::string simple_hash(std::string input) {
    unsigned long hash = 5381;
    for (char c : input) hash = ((hash << 5) + hash) + c;
    return std::to_string(hash);
}

int main() {
    WSADATA wsa;
    SOCKET s, new_socket;
    struct sockaddr_in server, client;
    int c;
    char message[2000];

    std::cout << "--- SENTIHEALTH NETWORKED SECURITY ENGINE ---" << std::endl;

    // 1. Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) return 1;

    // 2. Create Socket
    s = socket(AF_INET, SOCK_STREAM, 0);
    
    // 3. Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(5555); // We are listening on Port 5555

    // 4. Bind
    if (bind(s, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) return 1;

    listen(s, 3);
    std::cout << "[+] Server Listening on Port 5555... Waiting for Data." << std::endl;

    c = sizeof(struct sockaddr_in);
    while ((new_socket = accept(s, (struct sockaddr *)&client, &c)) != INVALID_SOCKET) {
        // Receive data from Python
        int recv_size = recv(new_socket, message, 2000, 0);
        if (recv_size > 0) {
            message[recv_size] = '\0';
            std::string raw_data(message);
            
            // Process (Hash) the data
            std::string hashed_data = simple_hash(raw_data);
            std::cout << "[SECURE] Received: " << raw_data << " -> Protected: " << hashed_data << std::endl;

            // Send back to Python
            send(new_socket, hashed_data.c_str(), hashed_data.length(), 0);
        }
        closesocket(new_socket);
    }

    closesocket(s);
    WSACleanup();
    return 0;
}