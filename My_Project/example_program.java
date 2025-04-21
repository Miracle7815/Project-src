package com.example.demo;       //注释

// 导入语句
import java.util.Arrays;
import java.util.List;             /*注释*/
import static java.lang.Math.PI;      //注释
 
/​**​
 * 这是一个演示Java各种语法结构的类
 * 包含文档注释示例
 */
public class JavaSyntaxDemo {
    
    // 类变量声明
    private static final String CLASS_NAME = "JavaSyntaxDemo";
    
    // 实例变量声明
    private int instanceVar = 10;
    
    // 主方法
    public static void main(String[] args) {
        // 局部变量声明
        int localVar = 5;
        String message = "Hello, Java!";
        
        // 打印语句
        System.out.println(message);
        
        // if语句
        if (localVar > 0) {
            System.out.println("localVar是正数");
        }
        
        // if-else语句
        if (localVar % 2 == 0) {
            System.out.println("localVar是偶数");
        } else {
            System.out.println("localVar是奇数");
        }
        
        // if-else if-else语句
        if (localVar < 0) {
            System.out.println("localVar是负数");
        } else if (localVar == 0) {
            System.out.println("localVar是零");
        } else {
            System.out.println("localVar是正数");
        }
        
        // switch语句
        switch (localVar) {
            case 1:
                System.out.println("localVar是1");
                break;
            case 5:
                System.out.println("localVar是5");
                break;
            default:
                System.out.println("localVar是其他值");
        }
        
        // for循环
        for (int i = 0; i < 3; i++) {
            System.out.println("for循环: i = " + i);
        }
        
        // 增强for循环
        List<String> fruits = Arrays.asList("Apple", "Banana", "Cherry");
        for (String fruit : fruits) {
            System.out.println("水果: " + fruit);
        }
        
        // while循环
        int whileCounter = 3;
        while (whileCounter > 0) {
            System.out.println("while循环: counter = " + whileCounter);
            whileCounter--;
        }
        
        // do-while循环
        int doWhileCounter = 3;
        do {
            System.out.println("do-while循环: counter = " + doWhileCounter);
            doWhileCounter--;
        } while (doWhileCounter > 0);
        
        // break语句
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                System.out.println("遇到5，使用break退出循环");
                break;
            }
            System.out.println("break测试: i = " + i);
        }
        
        // continue语句
        for (int i = 0; i < 5; i++) {
            if (i == 2) {
                System.out.println("遇到2，跳过本次循环");
                continue;
            }
            System.out.println("continue测试: i = " + i);
        }
        
        // 方法调用
        int sum = addNumbers(3, 4);
        System.out.println("3 + 4 = " + sum);
        
        // 静态导入使用
        System.out.println("PI的值: " + PI);
        
        // 异常处理
        try {
            int result = divide(10, 0);
            System.out.println("除法结果: " + result);
        } catch (ArithmeticException e) {
            System.out.println("捕获到算术异常: " + e.getMessage());
        } finally {
            System.out.println("finally块总是执行");
        }
        
        // 断言
        assert localVar == 5 : "localVar应该等于5";
        
        // 同步块
        synchronized (JavaSyntaxDemo.class) {
            System.out.println("进入同步块");
        }
        
        // lambda表达式
        Runnable runnable = () -> {
            System.out.println("这是一个lambda表达式");
        };
        new Thread(runnable).start();
        
        // throw语句
        try {
            validateAge(15);
        } catch (IllegalArgumentException e) {
            System.out.println("捕获到异常: " + e.getMessage());
        }
    }
    
    // 方法定义(带返回值)
    public static int addNumbers(int a, int b) {
        return a + b;
    }
    
    // 方法定义(带throws声明)
    public static int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("除数不能为零");
        }
        return a / b;
    }
    
    // 方法定义(带参数验证)
    public static void validateAge(int age) {
        if (age < 18) {
            throw new IllegalArgumentException("年龄必须大于等于18岁");
        }
        System.out.println("年龄验证通过");
    }
    
    // 静态初始化块
    static {
        System.out.println("静态初始化块执行");
    }
    
    // 实例初始化块
    {
        System.out.println("实例初始化块执行");
    }
}