---
title: "TD: Réseau"
author: "qkzk"
date: "2021/06/08"
theme: "metropolis"
weight: 11
bookCollapseSection: true

---

### pdf [pour impression](./td_reseau.pdf)

# Adresse IP

Soit l'adresse ip suivante :

192.16.5.133/24

1. Est-ce une adresse IPv4 ou IPv6 ? Justifier.
1. Combien de bits sont utilisés pour identifier l'adresse réseau ?
2. Combien de bits sont utilisés pour identifier la partie hôte ?
3. Écrire le masque de sous réseau au format décimal
4. L'adresse 192.16.5.130 figure-t-elle dans le même réseau ? Justifier.

# Adresse IP : masque de taille quelconque

On considère l'adresse IP 172.16.31.28/22

1. Convertir chaque nombre de l'adresse en binaire
2. Déterminer la partie réseau et la partie hôte.
3. Écrire le masque de sous réseau au format binaire.
4. Convertir chaque adresse : réseau, hôte et masque en décimal.
5. L'adresse 172.16.29.12/22 figure-t-elle dans le même réseau ?

# Commandes linux


1. Quelle commande linux permet de connaître la configuration réseau
  d'une machine ?
2. On souhaite connaître la latence entre notre machine et un serveur
  distant : 8.8.8.8

    Quelle commande saisir ?

3. On souhaite connaître le trajet emprunté entre notre machine et 
  le serveur distant précédent.

   Quelle commande saisir ? Verra-t-on toujours toutes les machines intermédiaires ?


# Analyser la sortie d'une commande

Voici la sortie d'une commande linux :

  ```
  eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether dc:a6:32:20:3c:96  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

  lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
          inet 127.0.0.1  netmask 255.0.0.0
          inet6 ::1  prefixlen 128  scopeid 0x10<host>
          loop  txqueuelen 1000  (Local Loopback)
          RX packets 4630776  bytes 249564311 (238.0 MiB)
          RX errors 0  dropped 0  overruns 0  frame 0
          TX packets 4630776  bytes 249564311 (238.0 MiB)
          TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

  wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
          inet 192.168.1.44  netmask 255.255.255.0  broadcast 192.168.1.255
          inet6 fe80::fa2f:4a2:7ed8:4e48  prefixlen 64  scopeid 0x20<link>
          inet6 2a01:cb0c:4e6:8100:6abd:71bb:51fa:5c7f  prefixlen 64  scopeid 0x0<global>
          ether dc:a6:32:20:3c:97  txqueuelen 1000  (Ethernet)
          RX packets 20239108  bytes 1207246530 (1.1 GiB)
          RX errors 0  dropped 12451  overruns 0  frame 0
          TX packets 27132557  bytes 2113882478 (1.9 GiB)
          TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  ```

1. Quelle commande a été tapée ?
2. À combien de réseau la machine est-elle raccordée ?

    Indiquer les adresses IPv4 de la machine sur chaque réseau.
    On précisera aussi le masque.

3. Le réseau `eth0` est-il actif ? Justifier.


# Analyser la sortie d'une commande

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.73 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=7.06 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=115 time=6.64 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 5ms
rtt min/avg/max/mdev = 6.639/7.810/9.730/1.368 m
```

1. Quelle commande a été tapée ?
2. Quel protocole utilise cette commande ?
2. Que mesurent les valeurs `time` indiquées aux lignes 2, 3 et 4 ?
3. Cette latence est-elle satisfaisante pour jouer aux jeux vidéos ?
4. Peut-on estimer le débit à l'aide de cette commande ?


# Analyser la sortie d'une commande

```
traceroute to 1.1.1.1 (1.1.1.1), 30 hops max, 60 byte packets
 1  * * *
 2  80.10.233.205 (80.10.233.205)  134.362 ms  136.719 ms  137.042 ms
 3  ae112-0.nclil101.rbci.orange.net (193.253.88.134)  136.986 ms  137.088 ms  137.036 ms
 4  ae41-0.nilil201.rbci.orange.net (81.253.129.30)  136.995 ms  136.916 ms  136.949 ms
 5  ae40-0.nilil202.rbci.orange.net (81.253.129.2)  137.123 ms  137.732 ms  137.682 ms
 6  81.253.184.118 (81.253.184.118)  137.640 ms  8.464 ms  7.261 ms
 7  193.251.129.79 (193.251.129.79)  8.305 ms ae300-0.ffttr6.frankfurt.opentransit.net (193.251.241.22)  16.879 ms 193.251.129.79 (193.251.129.79)  9.466 ms
 8  ae303-0.ffttr6.frankfurt.opentransit.net (193.251.243.248)  19.042 ms cloudflare-8.gw.opentransit.net (193.251.150.138)  17.997 ms ae303-0.ffttr6.frankfurt.opentransit.net (193.251.243.248)  19.994 ms
 9  cloudflare-8.gw.opentransit.net (193.251.150.138)  40.885 ms  40.481 ms one.one.one.one (1.1.1.1)  16.223 ms
```

1. Quelle comamnde a été tapée ?
2. Qu'indiquent les lignes intermédiaires ?
3. La machine utilisée pour taper cette commande est à Lille. Est-ce aussi le cas
  de la machine distante 1.1.1.1 ?


Voici une autre sortie similaire :

```
traceroute to google.com (216.58.214.78), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  2.692 ms  3.183 ms  3.349 ms
 2  80.10.233.205 (80.10.233.205)  4.865 ms  5.280 ms  5.815 ms
 3  ae112-0.nclil101.rbci.orange.net (193.253.88.134)  6.081 ms  6.045 ms  6.013 ms
 4  ae41-0.nilil201.rbci.orange.net (81.253.129.30)  6.524 ms  6.082 ms  6.520 ms
 5  81.253.184.178 (81.253.184.178)  12.069 ms  11.975 ms *
 6  72.14.219.248 (72.14.219.248)  9.386 ms 209.85.173.98 (209.85.173.98)  8.204 ms 72.14.219.248 (72.14.219.248)  7.035 ms
 7  * * *
 8  108.170.245.1 (108.170.245.1)  8.911 ms 142.250.224.93 (142.250.224.93)  8.530 ms 142.250.234.40 (142.250.234.40)  6.588 ms
 9  108.170.244.197 (108.170.244.197)  7.943 ms 108.170.245.6 (108.170.245.6)  6.461 ms 108.170.244.198 (108.170.244.198)  8.481 ms
10  72.14.238.55 (72.14.238.55)  8.440 ms 209.85.248.117 (209.85.248.117)  8.550 ms fra15s10-in-f78.1e100.net (216.58.214.78)  8.910 ms
```

1. Que penser de l'affirmation : "Quand je me connecte chez google, les paquets traversent l'Atlantique !" Justifier.




# Un réseau domestique

Le réseau domestique de Thibault est constitué des éléments suivants

| Machine             | Symbole | Adresse(s)                      | Liaison  | Raccordé à |
|---------------------|---------|---------------------------------|----------|------------|
| Box                 | B       | 192.168.0.1/24 et 88.12.13.21   | Optique  | Internet   |
| SmartTV             | TV      | 192.168.0.2/24                  | Wifi     | Box        |
| PC                  | PC      | 192.168.0.3/24                  | Ethernet | Box        |
| Smartphone          | TEL     | 192.168.0.4/24                  | Wifi     | Box        |
| Répéteur Wifi       | R       | 192.168.0.5/24 et 172.16.1.1/16 | Ethernet | Box        |
| CameraIP            | CAM     | 172.16.1.2/16                   | Wifi     | R          |
| Ordinateur portable | L       | 172.16.1.3/16                   | Wifi     | R          |

1. Deux machines disposent de plusieurs adresses IP. Quels sont leur rôle ?

2. Dessiner un plan du réseau.

    On utilisera le rouge pour le réseau principal, issu de la box et le bleu pour le réseau
    secondaire depuis le routeur R.

    On utilisera le trait plein pour une liaision filaire et les pointillés pour une liaision
    radio.

3. La camera CAM et l'ordinateur PC figurent-ils sur le même réseau ?

4. Thibault utilise son ordinateur portable pour naviguer sur internet.

    Dessiner le trajet d'un paquet sur son réseau jusqu'à internet.

5. Thibault souhaite installer un cluster constitué de 12 machines afin de faire du calcul
  en parallèle. Dispose-t-il d'assez d'adresses sur chacun de ses réseaux ?

6. Sur cette machine, il visite un site lui affichant son adresse IP.

    Que verra-t-il ? Pourquoi ?



