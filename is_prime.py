def is_prime(n):
    """
    숫자가 소수인지 확인하는 함수
    
    Args:
        n: 확인할 정수
        
    Returns:
        bool: 소수이면 True, 아니면 False
    """
    # 2 미만의 수는 소수가 아님
    if n < 2:
        return False
    
    # 2는 소수
    if n == 2:
        return True
    
    # 짝수는 소수가 아님
    if n % 2 == 0:
        return False
    
    # 3부터 n의 제곱근까지 홀수로 나누어 확인
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


def is_prime_optimized(n):
    """
    최적화된 소수 판별 함수 (더 빠른 성능)
    
    Args:
        n: 확인할 정수
        
    Returns:
        bool: 소수이면 True, 아니면 False
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 6k ± 1 형태로 확인 (모든 소수는 6k ± 1 형태)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


# 사용 예시
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 10, 11, 13, 15, 17, 20, 29, 100]
    
    print("=== 기본 버전 ===")
    for num in test_numbers:
        print(f"{num}: {'소수' if is_prime(num) else '소수 아님'}")
    
    print("\n=== 최적화 버전 ===")
    for num in test_numbers:
        print(f"{num}: {'소수' if is_prime_optimized(num) else '소수 아님'}")
