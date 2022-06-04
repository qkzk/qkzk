---
title: "viz.js"
weight: 100000000

---

# Graphe au format DOT avec viz.js

## Exemple 1

{{< graphviz title="Graphe orienté" >}}
digraph {
    a -> b
}
{{< /graphviz >}}

## Exemple 2

{{< graphviz title="Graphe contenant une erreur" >}}
digraph {
    a -> 
}
{{< /graphviz >}}

## Exemple 3

{{< graphviz title="Graphe simple">}}
graph {
    c -- d
    d -- e
    c -- e
}
{{< /graphviz >}}

## Exemple 4

{{< graphviz title="Finite State Machine" >}}
digraph finite_state_machine {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	rankdir=LR;
	node [shape = doublecircle]; 0 3 4 8;
	node [shape = circle];
	0 -> 2 [label = "SS(B)"];
	0 -> 1 [label = "SS(S)"];
	1 -> 3 [label = "S($end)"];
	2 -> 6 [label = "SS(b)"];
	2 -> 5 [label = "SS(a)"];
	2 -> 4 [label = "S(A)"];
	5 -> 7 [label = "S(b)"];
	5 -> 5 [label = "S(a)"];
	6 -> 6 [label = "S(b)"];
	6 -> 5 [label = "S(a)"];
	7 -> 8 [label = "S(b)"];
	7 -> 5 [label = "S(a)"];
	8 -> 6 [label = "S(b)"];
	8 -> 5 [label = "S(a)"];
}
{{< /graphviz >}}

## Exemple 5

{{< graphviz title="Linux Kernel Diagram" >}}
digraph "Linux_kernel_diagram" {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	graph [
		newrank = true,
		nodesep = 0.3,
		ranksep = 0.2,
		overlap = true,
		splines = false,
	]
	node [
		fixedsize = false,
		fontsize = 24,
		height = 1,
		shape = box,
		style = "filled,setlinewidth(5)",
		width = 2.2
	]
	edge [
		arrowhead = none,
		arrowsize = 0.5,
		labelfontname = "Ubuntu",
		weight = 10,
		style = "filled,setlinewidth(5)"
	]
	subgraph system {
		node [color = "#e27dd6ff"]
		edge [color = "#e27dd6ff"]
		system_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			shape = point
		]
		system [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/System",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		system -> system_ [
			arrowhead = "",
			row = func];
		SCI [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Syscalls",
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "System calls",
			row = usr,
			shape = ellipse]
		sysfs [
			fillcolor = "#b2d3e4",
			label = "proc & sysfs\nfile systems"]
		SCI -> sysfs
		DM [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "Device\nModel",
			shape = octagon,
			width = 2]
		sysfs -> DM
		log_sys [
			fillcolor = "#6a9ab1",
			fontsize = 20,
			label = "system run,\nmodules,\ngeneric\nHW access "]
		DM -> log_sys
		bus_drv [
			fillcolor = "#71809b",
			label = "bus drivers"]
		log_sys -> bus_drv
		buses [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "buses:\nPCI, USB ...",
			row = chip]
		bus_drv -> buses
	}
	subgraph networking {
		node [color = "#61c2c5"]
		edge [color = "#61c2c5"]
		networking_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			shape = point
				width = 0]
		networking [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Networking",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		networking -> networking_ [
			arrowhead = "",
			row = func]
		sock [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = Sockets,
			row = usr,
			shape = ellipse]
		prot_fam [
			fillcolor = "#b2d3e4",
			label = "protocol\nfamilies"]
		sock -> prot_fam
		log_prot [
			fillcolor = "#6a9ab1",
			label = "protocols:\nTCP, UDP, IP"]
		prot_fam -> log_prot
		netif [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "network\ninterfaces\nand drivers"]
		log_prot -> netif
		net_hw [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "network:\nEthernet, WiFi ...",
			row = chip]
		netif -> net_hw
		NFS [
			color = "#8383cc",
			fillcolor = "#91b5c9",
			fixedsize = true,
			height = 0.8,
			label = NFS,
			shape = octagon,
			width = 1.2]
		NFS -> log_prot [weight = 0]
	}
	subgraph processing {
		node [color = "#c46747"]
		edge [color = "#c46747"]
		processing_ [
			fixedsize = true,
			height = 0,
			shape = point
				style = invis,
			width = 0]
		processing [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Processing",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		processing -> processing_ [
			arrowhead = "",
			row = func]
		proc [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = Processes,
			row = usr,
			shape = ellipse]
		Tasks [
			fillcolor = "#b2d3e4"]
		proc -> Tasks
		sync [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			fontname = "Arial Narrow"
			label = synchronization,
			height = 0.7,
			//width = 2,
			shape = octagon]
		Tasks -> sync
		sched [
			fillcolor = "#6a9ab1",
			label = Scheduler]
		sync -> sched
		IRQ [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "interrupts\ncore,\nCPU arch"]
		sched -> IRQ
		CPU [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			row = chip]
		IRQ -> CPU
	}	// processing
	subgraph mem {
		node [
			color = "#51bf5b",
			height = 1
		]
		edge [color = "#51bf5b"]
		MA [
			color = "#51bf5b",
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "memory\naccess",
			row = usr,
			height = 1,
			shape = ellipse]
		MA -> VM
		mmap [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "memory\nmapping",
			shape = octagon,
			width = 2]
		mmap -> log_mem
		log_mem -> PA
		SW [
			color = "#8383cc",
			fillcolor = "#91b5c9",
			fixedsize = true,
			label = Swap,
			height = 0.8,
			shape = octagon,
			width = 1.2]
		mmap -> SW [weight = 1]
		SW -> block [
			color = "#8383cc", weight = 1]
		PA [
			fillcolor = "#71809b",
			label = "Page\nAllocator"
		]
		PC -> PA [weight = 0 color="#51bf5b"]
		RAM [
			color = "#51bf5b",
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "MMU, RAM",
			height = 1,
			row = chip]
		PA -> RAM
		memory -> memory_ [
			arrowhead = "",
			row = func]
		VM -> mmap
	}	// mem
	subgraph storage {
		node [color = "#8383cc"]
		edge [color = "#8383cc"]
		NFS;
		storage_ [
			shape = point,
			fixedsize = true,
			height = 0,
			style = invis,
			width = 0]
		storage [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Storage",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		storage -> storage_ [
			arrowhead = "",
			row = func]
		FS [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "files and\ndirectories",
			row = usr,
			shape = ellipse]
		VFS [
			fillcolor = "#b2d3e4",
			label = "Virtual\nFile System"]
		FS -> VFS
		VFS -> mmap [weight = 0]
		VFS -> NFS [weight = 0]
		logFS [
			fillcolor = "#6a9ab1",
			fontsize = 20,
			label = "logical\nfilesystems:\next3, xfs ..."]
		VFS -> logFS
		PC [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "page\ncache",
			shape = octagon,
			width = 1.2]
		VFS -> PC [weight = 0]
		block [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "Block\ndevices\nand drivers"]
		logFS -> block
		SD [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "storage devices:\nSCSI, NVMe ...",
			row = chip]
		block -> SD
	}	// storge
	subgraph HI {
		node [color = "#cfbf57ff"]
		edge [
			color = "#cfbf57ff",
			weight = 10
		]
		HI_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		HI [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Human_interfaces",
			fillcolor = white,
			fixedsize = true,
			fontsize = 12,
			height = 0.6,
			label = "human\ninterface",
			row = func,
			width = 2]
		HI -> HI_ [
			arrowhead = "",
			row = func]
		char [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "char\ndevices",
			row = usr,
			shape = ellipse]
		input [
			fillcolor = "#b2d3e4",
			label = "input\nsubsystem"]
		char -> input
		F7 [
			fillcolor = "#6a9ab1",
			label = "HI class\ndrivers"]
		input -> F7
		HID [
			fillcolor = "#71809b",
			fontsize = 20,
			URL = "https://www.kernel.org/doc/html/latest/hid/",
			label = "HI\nperipherals\ndrivers"]
		F7 -> HID
		display [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 19,
			label = "keyboard, mouse,\ndisplay, audio",
			row = chip]
		HID -> display
	} // HI
	subgraph functions {
		graph [rank = same]
		edge [
			style = invis,
			weight = 1
		]
		system;
		networking;
		system -> processing [weight = 1]
		storage -> networking [weight = 1]
		memory [
			color = "#51bf5b",
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Memory",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		memory -> storage [weight = 1]
		processing -> memory [weight = 1]
		functions_ [
			fixedsize = true,
			height = 0,
			shape = point
			style = invis,
			width = 0]
		functions_ -> HI -> system [weight = 1]
		functions [
			color = gray,
			tooltip = "Columns represent main functionalities of the kernel",
			URL = "http://www.makelinux.net/ldd3/chp-1-sect-2.shtml",
			fillcolor = gray,
			fixedsize = true,
			height = 0.6,
			row = func,
			style = dashed,
			width = 1.6]
		functions -> functions_ [
			arrowhead = "",
			color = gray,
			style = "",
			weight = ""]
	}
	subgraph interfaces {
		graph [rank = same]
		SCI;
		sock;
		FS;
		proc;
		char;
		usr_ [
			fixedsize = true,
			height = 0,
			shape = point
				style = invis,
			width = 0.5]
		usr [
			fillcolor = "#d9e7eeff",
			fixedsize = true,
			label = "user space\ninterfaces",
			row = usr,
			shape = ellipse,
			style = "filled,setlinewidth(0)"]
		MA;
	}
	{
		edge [style = invis weight = 10 ]
		system_;
		SCI;
		system_ -> SCI;
		networking_;
		sock;
		networking_ -> sock;
		storage_;
		FS;
		storage_ -> FS;
		processing_;
		proc;
		processing_ -> proc;
		HI_;
		char;
		HI_ -> char;
		MA;
		memory_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		memory_ -> MA;
	}
	subgraph virtual {
		graph [rank = same]
		sysfs;
		prot_fam;
		VFS;
		Tasks;
		input;
		D0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		virt [
			fillcolor = "#b2d3e4",
			label = "virtual\nsubsystems",
			URL = "https://en.wikipedia.org/wiki/Proxy_pattern",
			tooltip = "proxy between standard user space interfaces and internal implementations",
			style = "filled,setlinewidth(0)"]
		VM [
			color = "#51bf5b",
			fillcolor = "#b2d3e4",
			label = "Virtual\nmemory"]
	}
	subgraph bridges {
		graph [rank = same]
		bridges [
			fillcolor = "#91b5c9",
			shape = octagon,
			tooltip = "bridges between uniform virtual interfaces and various implementations",
			URL = "https://en.wikipedia.org/wiki/Bridge_pattern",
			style = "filled,setlinewidth(0)"]
		DM;
		NFS;
		mmap;
		sync;
		E0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		//PC
	}
	subgraph logical {
		graph [rank = same]
		log_sys;
		log_prot;
		logFS;
		sched;
		F7;
		F0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		logical [
			fillcolor = "#6a9ab1",
			style = "filled,setlinewidth(0)"]
		log_mem [
			color = "#51bf5b",
			fillcolor = "#6a9ab1",
			label = "logical\nmemory"]
		//SW
	}
	subgraph HWI {
		graph [rank = same]
		HWI [
			fillcolor = "#71809b",
			label = "hardware\ninterfaces",
			style = "filled,setlinewidth(0)"]
		bus_drv;
		netif;
		block;
		//PA;
		IRQ;
		HID;
		G0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
	}
	subgraph HW {
		graph [rank = same]
		HW [
			fillcolor = "#777777",
			fontcolor = white,
			label = "electronics,\nhardware",
			row = chip,
			style = "filled,setlinewidth(0)"]
		buses;
		net_hw;
		SD;
		CPU;
		display;
		H0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		RAM;
	}
	bottom [
		label = "© 2007-2022 Costa Shulyupin http://www.MakeLinux.net/kernel/diagram",
		URL = "http://www.MakeLinux.net/kernel/diagram",
		shape = plaintext,
		style = ""]
	CPU -> bottom [style = invis]
	layers [
		fillcolor = lightgray,
		tooltip = "Functionalities are divided to common layers. It is approximate division.",
		height = 0.1,
		style = "filled,setlinewidth(0)",
		width = 0.5]
	functions -> layers [style = invis ]
	usr -> usr_ [
		arrowhead = "",
		color = "#d9e7eeff",
		minlen = 2]
	usr -> virt [
		color = "#d9e7eeff"]
	virt -> D0 [
		arrowhead = "",
		color = "#b2d3e4",
		minlen = 2]
	virt -> bridges [
		color = "#b2d3e4"]
	bridges -> E0 [
		arrowhead = "",
		color = "#91b5c9",
		minlen = 2,
		style = "filled,setlinewidth(6)",
		weight = ""]
	bridges -> logical [
		color = "#91b5c9",
		style = "filled,setlinewidth(6)"]
	logical -> F0 [
		arrowhead = "",
		color = "#6a9ab1",
		minlen = 2,
		row = logical,
		style = "filled,setlinewidth(6)",
		weight = ""]
	logical -> HWI [
		color = "#6a9ab1",
		row = logical,
		style = "filled,setlinewidth(6)"]
	HWI -> G0 [
		arrowhead = "",
		color = "#71809b",
		minlen = 2,
		row = HWI,
		style = "filled,setlinewidth(6)",
		weight = ""]
	HWI -> HW [
		color = "#71809b",
		row = HWI,
		style = "filled,setlinewidth(6)"]
	HW -> H0 [
		arrowhead = "",
		color = "#777777",
		minlen = 2,
		row = chip,
		style = "filled,setlinewidth(6)",
		weight = ""]
	layers -> usr [
		arrowhead = "",
		color = gray,
		style = "filled,setlinewidth(1)"]
	LKD [
		fontsize = 40,
		label = "Linux kernel diagram",
		shape = plain,
		style = ""]
	LKD -> processing [style = invis]
}
{{< /graphviz >}}

## Exemple 6

{{< graphviz title="Cluster" >}}
digraph G {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]

	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		a0 -> a1 -> a2 -> a3;
		label = "process #1";
	}

	subgraph cluster_1 {
		node [style=filled];
		b0 -> b1 -> b2 -> b3;
		label = "process #2";
		color=blue
	}
	start -> a0;
	start -> b0;
	a1 -> b3;
	b2 -> a3;
	a3 -> a0;
	a3 -> end;
	b3 -> end;

	start [shape=Mdiamond];
	end [shape=Msquare];
}
{{< /graphviz >}}

## Exemple 7

{{< graphviz title="ninja" >}}
digraph ninja {
fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]
rankdir="LR"
node [fontsize=10, shape=box, height=0.25]
edge [fontsize=10]
"0x7fe58d50f070" [label="all"]
"0x7fe58d50eeb0" [label="phony", shape=ellipse]
"0x7fe58d50eeb0" -> "0x7fe58d50f070"
"0x7fe58d5092d0" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50b640" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50bc10" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d508820" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50c0a0" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50c470" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50c880" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d50cc10" -> "0x7fe58d50eeb0" [arrowhead=none]
"0x7fe58d5092d0" [label="ninja"]
"0x7fe58d509260" [label="link", shape=ellipse]
"0x7fe58d509260" -> "0x7fe58d5092d0"
"0x7fe58d508ef0" -> "0x7fe58d509260" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d509260" [arrowhead=none]
"0x7fe58d508ef0" [label="build/ninja.o"]
"0x7fe58d508c50" -> "0x7fe58d508ef0" [label=" cxx"]
"0x7fe58d508c50" [label="src/ninja.cc"]
"0x7fe58d508f80" [label="build/libninja.a"]
"0x7fe58d508e00" [label="ar", shape=ellipse]
"0x7fe58d508e00" -> "0x7fe58d508f80"
"0x7fe58d505cb0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d505e40" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d506020" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5061e0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5063d0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5065e0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5067a0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d506a00" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d506b60" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d506d40" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d506ee0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507160" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507320" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5074e0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5076a0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507950" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507ad0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507ce0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507ea0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d508000" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5081c0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d508400" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d5085a0" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d507080" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d508b10" -> "0x7fe58d508e00" [arrowhead=none]
"0x7fe58d505cb0" [label="build/browse.o"]
"0x7fe58d505910" [label="cxx", shape=ellipse]
"0x7fe58d505910" -> "0x7fe58d505cb0"
"0x7fe58d505d10" -> "0x7fe58d505910" [arrowhead=none]
"0x7fe58d505a40" -> "0x7fe58d505910" [arrowhead=none style=dotted]
"0x7fe58d505d10" [label="src/browse.cc"]
"0x7fe58d505a40" [label="build/browse_py.h"]
"0x7fe58d5059d0" [label="inline", shape=ellipse]
"0x7fe58d5059d0" -> "0x7fe58d505a40"
"0x7fe58d505aa0" -> "0x7fe58d5059d0" [arrowhead=none]
"0x7fe58d505b40" -> "0x7fe58d5059d0" [arrowhead=none]
"0x7fe58d505aa0" [label="src/browse.py"]
"0x7fe58d505b40" [label="src/inline.sh"]
"0x7fe58d505e40" [label="build/build.o"]
"0x7fe58d505f00" -> "0x7fe58d505e40" [label=" cxx"]
"0x7fe58d505f00" [label="src/build.cc"]
"0x7fe58d506020" [label="build/build_log.o"]
"0x7fe58d5060c0" -> "0x7fe58d506020" [label=" cxx"]
"0x7fe58d5060c0" [label="src/build_log.cc"]
"0x7fe58d5061e0" [label="build/clean.o"]
"0x7fe58d506280" -> "0x7fe58d5061e0" [label=" cxx"]
"0x7fe58d506280" [label="src/clean.cc"]
"0x7fe58d5063d0" [label="build/clparser.o"]
"0x7fe58d505ea0" -> "0x7fe58d5063d0" [label=" cxx"]
"0x7fe58d505ea0" [label="src/clparser.cc"]
"0x7fe58d5065e0" [label="build/debug_flags.o"]
"0x7fe58d506680" -> "0x7fe58d5065e0" [label=" cxx"]
"0x7fe58d506680" [label="src/debug_flags.cc"]
"0x7fe58d5067a0" [label="build/depfile_parser.o"]
"0x7fe58d506870" -> "0x7fe58d5067a0" [label=" cxx"]
"0x7fe58d506870" [label="src/depfile_parser.cc"]
"0x7fe58d506a00" [label="build/deps_log.o"]
"0x7fe58d506a60" -> "0x7fe58d506a00" [label=" cxx"]
"0x7fe58d506a60" [label="src/deps_log.cc"]
"0x7fe58d506b60" [label="build/disk_interface.o"]
"0x7fe58d506c30" -> "0x7fe58d506b60" [label=" cxx"]
"0x7fe58d506c30" [label="src/disk_interface.cc"]
"0x7fe58d506d40" [label="build/dyndep.o"]
"0x7fe58d506dd0" -> "0x7fe58d506d40" [label=" cxx"]
"0x7fe58d506dd0" [label="src/dyndep.cc"]
"0x7fe58d506ee0" [label="build/dyndep_parser.o"]
"0x7fe58d5070f0" -> "0x7fe58d506ee0" [label=" cxx"]
"0x7fe58d5070f0" [label="src/dyndep_parser.cc"]
"0x7fe58d507160" [label="build/edit_distance.o"]
"0x7fe58d507200" -> "0x7fe58d507160" [label=" cxx"]
"0x7fe58d507200" [label="src/edit_distance.cc"]
"0x7fe58d507320" [label="build/eval_env.o"]
"0x7fe58d5073c0" -> "0x7fe58d507320" [label=" cxx"]
"0x7fe58d5073c0" [label="src/eval_env.cc"]
"0x7fe58d5074e0" [label="build/graph.o"]
"0x7fe58d507580" -> "0x7fe58d5074e0" [label=" cxx"]
"0x7fe58d507580" [label="src/graph.cc"]
"0x7fe58d5076a0" [label="build/graphviz.o"]
"0x7fe58d507740" -> "0x7fe58d5076a0" [label=" cxx"]
"0x7fe58d507740" [label="src/graphviz.cc"]
"0x7fe58d507950" [label="build/lexer.o"]
"0x7fe58d5079c0" -> "0x7fe58d507950" [label=" cxx"]
"0x7fe58d5079c0" [label="src/lexer.cc"]
"0x7fe58d507ad0" [label="build/line_printer.o"]
"0x7fe58d507b40" -> "0x7fe58d507ad0" [label=" cxx"]
"0x7fe58d507b40" [label="src/line_printer.cc"]
"0x7fe58d507ce0" [label="build/manifest_parser.o"]
"0x7fe58d507d60" -> "0x7fe58d507ce0" [label=" cxx"]
"0x7fe58d507d60" [label="src/manifest_parser.cc"]
"0x7fe58d507ea0" [label="build/metrics.o"]
"0x7fe58d507f00" -> "0x7fe58d507ea0" [label=" cxx"]
"0x7fe58d507f00" [label="src/metrics.cc"]
"0x7fe58d508000" [label="build/parser.o"]
"0x7fe58d5080a0" -> "0x7fe58d508000" [label=" cxx"]
"0x7fe58d5080a0" [label="src/parser.cc"]
"0x7fe58d5081c0" [label="build/state.o"]
"0x7fe58d508260" -> "0x7fe58d5081c0" [label=" cxx"]
"0x7fe58d508260" [label="src/state.cc"]
"0x7fe58d508400" [label="build/string_piece_util.o"]
"0x7fe58d508480" -> "0x7fe58d508400" [label=" cxx"]
"0x7fe58d508480" [label="src/string_piece_util.cc"]
"0x7fe58d5085a0" [label="build/util.o"]
"0x7fe58d506f70" -> "0x7fe58d5085a0" [label=" cxx"]
"0x7fe58d506f70" [label="src/util.cc"]
"0x7fe58d507080" [label="build/version.o"]
"0x7fe58d508970" -> "0x7fe58d507080" [label=" cxx"]
"0x7fe58d508970" [label="src/version.cc"]
"0x7fe58d508b10" [label="build/subprocess-posix.o"]
"0x7fe58d508b90" -> "0x7fe58d508b10" [label=" cxx"]
"0x7fe58d508b90" [label="src/subprocess-posix.cc"]
"0x7fe58d50b640" [label="ninja_test"]
"0x7fe58d50b5c0" [label="link", shape=ellipse]
"0x7fe58d50b5c0" -> "0x7fe58d50b640"
"0x7fe58d5093e0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d509570" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d509710" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d507850" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d509c10" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d509df0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d509fe0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50a1b0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50a3b0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50a5b0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50a710" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50a970" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50ab10" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50ac90" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50aef0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50b0d0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50b290" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d50b3f0" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50b5c0" [arrowhead=none]
"0x7fe58d5093e0" [label="build/build_log_test.o"]
"0x7fe58d509470" -> "0x7fe58d5093e0" [label=" cxx"]
"0x7fe58d509470" [label="src/build_log_test.cc"]
"0x7fe58d509570" [label="build/build_test.o"]
"0x7fe58d509600" -> "0x7fe58d509570" [label=" cxx"]
"0x7fe58d509600" [label="src/build_test.cc"]
"0x7fe58d509710" [label="build/clean_test.o"]
"0x7fe58d5097b0" -> "0x7fe58d509710" [label=" cxx"]
"0x7fe58d5097b0" [label="src/clean_test.cc"]
"0x7fe58d507850" [label="build/clparser_test.o"]
"0x7fe58d5078f0" -> "0x7fe58d507850" [label=" cxx"]
"0x7fe58d5078f0" [label="src/clparser_test.cc"]
"0x7fe58d509c10" [label="build/depfile_parser_test.o"]
"0x7fe58d509c90" -> "0x7fe58d509c10" [label=" cxx"]
"0x7fe58d509c90" [label="src/depfile_parser_test.cc"]
"0x7fe58d509df0" [label="build/deps_log_test.o"]
"0x7fe58d509e50" -> "0x7fe58d509df0" [label=" cxx"]
"0x7fe58d509e50" [label="src/deps_log_test.cc"]
"0x7fe58d509fe0" [label="build/dyndep_parser_test.o"]
"0x7fe58d50a040" -> "0x7fe58d509fe0" [label=" cxx"]
"0x7fe58d50a040" [label="src/dyndep_parser_test.cc"]
"0x7fe58d50a1b0" [label="build/disk_interface_test.o"]
"0x7fe58d50a250" -> "0x7fe58d50a1b0" [label=" cxx"]
"0x7fe58d50a250" [label="src/disk_interface_test.cc"]
"0x7fe58d50a3b0" [label="build/edit_distance_test.o"]
"0x7fe58d50a450" -> "0x7fe58d50a3b0" [label=" cxx"]
"0x7fe58d50a450" [label="src/edit_distance_test.cc"]
"0x7fe58d50a5b0" [label="build/graph_test.o"]
"0x7fe58d50a610" -> "0x7fe58d50a5b0" [label=" cxx"]
"0x7fe58d50a610" [label="src/graph_test.cc"]
"0x7fe58d50a710" [label="build/lexer_test.o"]
"0x7fe58d50a7b0" -> "0x7fe58d50a710" [label=" cxx"]
"0x7fe58d50a7b0" [label="src/lexer_test.cc"]
"0x7fe58d50a970" [label="build/manifest_parser_test.o"]
"0x7fe58d50a9f0" -> "0x7fe58d50a970" [label=" cxx"]
"0x7fe58d50a9f0" [label="src/manifest_parser_test.cc"]
"0x7fe58d50ab10" [label="build/ninja_test.o"]
"0x7fe58d50ab70" -> "0x7fe58d50ab10" [label=" cxx"]
"0x7fe58d50ab70" [label="src/ninja_test.cc"]
"0x7fe58d50ac90" [label="build/state_test.o"]
"0x7fe58d50ad30" -> "0x7fe58d50ac90" [label=" cxx"]
"0x7fe58d50ad30" [label="src/state_test.cc"]
"0x7fe58d50aef0" [label="build/string_piece_util_test.o"]
"0x7fe58d50af70" -> "0x7fe58d50aef0" [label=" cxx"]
"0x7fe58d50af70" [label="src/string_piece_util_test.cc"]
"0x7fe58d50b0d0" [label="build/subprocess_test.o"]
"0x7fe58d50b150" -> "0x7fe58d50b0d0" [label=" cxx"]
"0x7fe58d50b150" [label="src/subprocess_test.cc"]
"0x7fe58d50b290" [label="build/test.o"]
"0x7fe58d50b2f0" -> "0x7fe58d50b290" [label=" cxx"]
"0x7fe58d50b2f0" [label="src/test.cc"]
"0x7fe58d50b3f0" [label="build/util_test.o"]
"0x7fe58d50b490" -> "0x7fe58d50b3f0" [label=" cxx"]
"0x7fe58d50b490" [label="src/util_test.cc"]
"0x7fe58d50bc10" [label="build_log_perftest"]
"0x7fe58d50bba0" [label="link", shape=ellipse]
"0x7fe58d50bba0" -> "0x7fe58d50bc10"
"0x7fe58d50b990" -> "0x7fe58d50bba0" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50bba0" [arrowhead=none]
"0x7fe58d50b990" [label="build/build_log_perftest.o"]
"0x7fe58d50ba20" -> "0x7fe58d50b990" [label=" cxx"]
"0x7fe58d50ba20" [label="src/build_log_perftest.cc"]
"0x7fe58d508820" [label="canon_perftest"]
"0x7fe58d5087b0" [label="link", shape=ellipse]
"0x7fe58d5087b0" -> "0x7fe58d508820"
"0x7fe58d50bd20" -> "0x7fe58d5087b0" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d5087b0" [arrowhead=none]
"0x7fe58d50bd20" [label="build/canon_perftest.o"]
"0x7fe58d508660" -> "0x7fe58d50bd20" [label=" cxx"]
"0x7fe58d508660" [label="src/canon_perftest.cc"]
"0x7fe58d50c0a0" [label="depfile_parser_perftest"]
"0x7fe58d50c030" [label="link", shape=ellipse]
"0x7fe58d50c030" -> "0x7fe58d50c0a0"
"0x7fe58d50bdf0" -> "0x7fe58d50c030" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50c030" [arrowhead=none]
"0x7fe58d50bdf0" [label="build/depfile_parser_perftest.o"]
"0x7fe58d50be70" -> "0x7fe58d50bdf0" [label=" cxx"]
"0x7fe58d50be70" [label="src/depfile_parser_perftest.cc"]
"0x7fe58d50c470" [label="hash_collision_bench"]
"0x7fe58d50c400" [label="link", shape=ellipse]
"0x7fe58d50c400" -> "0x7fe58d50c470"
"0x7fe58d50c270" -> "0x7fe58d50c400" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50c400" [arrowhead=none]
"0x7fe58d50c270" [label="build/hash_collision_bench.o"]
"0x7fe58d50c2d0" -> "0x7fe58d50c270" [label=" cxx"]
"0x7fe58d50c2d0" [label="src/hash_collision_bench.cc"]
"0x7fe58d50c880" [label="manifest_parser_perftest"]
"0x7fe58d50c810" [label="link", shape=ellipse]
"0x7fe58d50c810" -> "0x7fe58d50c880"
"0x7fe58d50c5e0" -> "0x7fe58d50c810" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50c810" [arrowhead=none]
"0x7fe58d50c5e0" [label="build/manifest_parser_perftest.o"]
"0x7fe58d50c670" -> "0x7fe58d50c5e0" [label=" cxx"]
"0x7fe58d50c670" [label="src/manifest_parser_perftest.cc"]
"0x7fe58d50cc10" [label="clparser_perftest"]
"0x7fe58d50cba0" [label="link", shape=ellipse]
"0x7fe58d50cba0" -> "0x7fe58d50cc10"
"0x7fe58d50c9c0" -> "0x7fe58d50cba0" [arrowhead=none]
"0x7fe58d508f80" -> "0x7fe58d50cba0" [arrowhead=none]
"0x7fe58d50c9c0" [label="build/clparser_perftest.o"]
"0x7fe58d50ca20" -> "0x7fe58d50c9c0" [label=" cxx"]
"0x7fe58d50ca20" [label="src/clparser_perftest.cc"]
}
{{< /graphviz >}}
