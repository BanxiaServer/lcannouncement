# 多个字符替换 搭配vscod使用 输出内容在控制台 只需要把 修改后的 Base64 字符串 复制替换掉核心源码中原来的字符串即可
# https://www.toolhelper.cn/EncodeDecode/Base64EncodeDecode base64编码/解码 预览更改 网站
# 有字数限制 要保证解码预览utf-8时最后结尾有这三个字符[סR�] 一定不要写超了
import base64

# 原始的 Base64 编码字符串 ser全局搜索这个字符串即可找到要更改的文件 
#           ↓从这里开始内容不同                     ↓从这里开始内容相同
#1.6 nXTHFAAGAAAAAACzWrABcAB4/7/K84SjAiAAKAFIZBABCpsBTFVOQVJDT1JFIElTIEEgRlJFRSBTT0ZUV0FSRS4gSUYgWU9VIFBBSUQgRk9SIElULCBZT1UgSEFWRSBCRUVOIFNDQU1NRUQhIGx1bmFyY29yZSDmmK/kuIDmrL7lhY3otLnova/ku7bjgILlpoLmnpzkvaDoirHpkrHkubDkuoblroPvvIzpgqPkvaDlsLHooqvpqpfkuobvvIHXoVLI
#2.0 nXTHFAAKAAAAAACzIrABGAEgZDj/v8rzhKMCQABIAGAAepsBTFVOQVJDT1JFIElTIEEgRlJFRSBTT0ZUV0FSRS4gSUYgWU9VIFBBSUQgRk9SIElULCBZT1UgSEFWRSBCRUVOIFNDQU1NRUQhIGx1bmFyY29yZSDmmK/kuIDmrL7lhY3otLnova/ku7bjgILlpoLmnpzkvaDoirHpkrHkubDkuoblroPvvIzpgqPkvaDlsLHooqvpqpfkuobvvIHXoVLI

#16进制编码
#每个版本的编码都不一样                                                     ↓从这里开始内容相同
#1.5 9D74C71400060000000000B35AB001700078FFBFCAF384A30220002801486410010A9B014C554E4152434F52452049532041204652454520534F4654574152452E20494620594F55205041494420464F522049542C20594F552048415645204245454E205343414D4D454421206C756E6172636F726520E698AFE4B880E6ACBEE5858DE8B4B9E8BDAFE4BBB6E38082E5A682E69E9CE4BDA0E88AB1E992B1E4B9B0E4BA86E5AE83EFBC8CE982A3E4BDA0E5B0B1E8A2ABE9AA97E4BA86EFBC81D7A152C8
#1.6 9D74C714000A0000000000B322B0011801206438FFBFCAF384A3024000480060007A9B014C554E4152434F52452049532041204652454520534F4654574152452E20494620594F55205041494420464F522049542C20594F552048415645204245454E205343414D4D454421206C756E6172636F726520E698AFE4B880E6ACBEE5858DE8B4B9E8BDAFE4BBB6E38082E5A682E69E9CE4BDA0E88AB1E992B1E4B9B0E4BA86E5AE83EFBC8CE982A3E4BDA0E5B0B1E8A2ABE9AA97E4BA86EFBC81D7A152C8
# D7A152C8 重要信息

original_base64_string = "nXTHFAAKAAAAAACzIrABGAEgZDj/v8rzhKMCQABIAGAAepsBTFVOQVJDT1JFIElTIEEgRlJFRSBTT0ZUV0FSRS4gSUYgWU9VIFBBSUQgRk9SIElULCBZT1UgSEFWRSBCRUVOIFNDQU1NRUQhIGx1bmFyY29yZSDmmK/kuIDmrL7lhY3otLnova/ku7bjgILlpoLmnpzkvaDoirHpkrHkubDkuoblroPvvIzpgqPkvaDlsLHooqvpqpfkuobvvIHXoVLI"

# 将 Base64 字符串解码为字节数据
original_byte_data = base64.b64decode(original_base64_string)

# 展示修改前的字节数据
print("未修改前的字节数据:", original_byte_data)

# 修改字节数据中的一段内容 在这里写出想要更改公告的内容***************************
replacement_text = "半夏公益服官方一群154422757 任何个人二维码的赞助都是假的 不要相信 我们也从来不会去售卖任何虚拟物品 不要被骗!"
#半夏备份 replacement_text = "半夏公益服官方一群154422757 任何个人二维码的赞助都是假的 不要相信 我们也从来不会去售卖任何虚拟物品 不要被骗!"
# HXoVLI
replacement_bytes = replacement_text.encode('utf-8')
original_byte_data_modified = bytearray(original_byte_data)
start_offset = 36  # 替换的起始位置
original_byte_data_modified[start_offset:start_offset + len(replacement_bytes)] = replacement_bytes

# 展示修改后的字节数据
print("修改后的字节数据:", original_byte_data_modified)

# 将修改后的字节数据编码为 Base64 字符串
modified_base64_string = base64.b64encode(original_byte_data_modified).decode()

# 展示修改后的 Base64 字符串
print("修改后的 Base64 字符串:", modified_base64_string)

'''
废弃内容 废弃内容 废弃内容
废弃内容 废弃内容 废弃内容
废弃内容 废弃内容 废弃内容
单个字符替换
import base64

# 原始的 Base64 编码字符串
original_base64_string = "nXTHFAAGAAAAAACzWrABcAB4/7/K84SjAiAAKAFIZBABCpsBTFVOQVJDT1JFIElTIEEgRlJFRSBTT0ZUV0FSRS4gSUYgWU9VIFBBSUQgRk9SIElULCBZT1UgSEFWRSBCRUVOIFNDQU1NRUQhIGx1bmFyY29yZSDmmK/kuIDmrL7lhY3otLnova/ku7bjgILlpoLmnpzkvaDoirHpkrHkubDkuoblroPvvIzpgqPkvaDlsLHooqvpqpfkuobvvIHXoVLI"

# 将 Base64 字符串解码为字节数据
original_byte_data = base64.b64decode(original_base64_string)

# 展示未修改前的字节数据
print("未修改前的字节数据:", original_byte_data)

# 修改字节数据中的一个字符，这里将第一个字符修改为 'A'
original_byte_data_modified = bytearray(original_byte_data)
original_byte_data_modified[36] = ord('L')

# 展示修改前和修改后的字节数据
print("修改前的字节数据:", original_byte_data)
print("修改后的字节数据:", original_byte_data_modified)

# 将修改后的字节数据编码为 Base64 字符串
modified_base64_string = base64.b64encode(original_byte_data_modified).decode()

# 展示修改后的 Base64 字符串
print("修改后的 Base64 字符串:", modified_base64_string)
'''
