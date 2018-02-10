[root@primarynode project-2]# tree
.
├── group_vars
│   └── all
├── main.retry
├── main.yml
├── roles
│   ├── module-1
│   │   ├── files
│   │   ├── handler
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   ├── common
│   │   │   │   ├── one.yml
│   │   │   │   ├── three.yml
│   │   │   │   └── two.yml
│   │   │   ├── main.yml
│   │   │   └── sub-module-1
│   │   │       └── submod1.yml
│   │   └── templates
│   │       ├── sub-mod-1.txt
│   │       ├── submod1.txt
│   │       ├── test_1.txt
│   │       ├── test_2.txt
│   │       ├── test_3.txt
│   │       ├── test_4.txt
│   │       └── test.txt
│   └── module-2
│       ├── files
│       ├── handler
│       │   └── main.yml
│       ├── tasks
│       │   └── main.yml
│       └── templates
│           ├── sec.txt
│           ├── test_2.txt
│           └── test.txt
├── submod1.txt
└── test_1.txt

14 directories, 23 files
