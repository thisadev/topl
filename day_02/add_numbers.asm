default rel             ; Use RIP-relative addressing by default

section .data align=8   ; Align data section to 8 bytes
    num1: db 5         ; First number
    align 8           ; Align next variable
    num2: db 3         ; Second number
    align 8           ; Align next variable
    result: db 0       ; To store the result
    align 8           ; Align next variable
    msg: db "Result: %d", 10, 0  ; Added newline (10)

section .text align=8   ; Align text section
    global _main       ; Entry point for macOS
    extern _exit       ; Import exit from libc
    extern _printf     ; Import printf function

_main:
    push    rbp        ; Set up stack frame
    mov     rbp, rsp

    ; Load and add numbers
    movzx   eax, byte [num1]    ; Load num1 into EAX with zero extension
    movzx   ecx, byte [num2]    ; Load num2 into ECX with zero extension
    add     eax, ecx            ; Add numbers
    mov     [result], al        ; Store result

    ; Call printf
    lea     rdi, [msg]          ; First argument: format string
    movzx   esi, byte [result]  ; Second argument: result value
    xor     eax, eax            ; Clear AL (no floating point args)
    call    _printf

    ; Exit program
    xor     edi, edi            ; Return code 0
    call    _exit

section .bss align=8    ; Align bss section
    output: resb 8     ; Align buffer to 8 bytes
