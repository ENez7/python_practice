from models.professional import Professional

def main():
    professional_1 = Professional('John', 30, 'Software Engineer')
    professional_2 = Professional('Jane', 25, 'Software Engineer')
    
    print(professional_1.getProfession())
    print(professional_2)

if __name__ == '__main__':
    main()