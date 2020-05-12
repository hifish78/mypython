class Solution:
    def validate_ip_address(self, IP: str) -> str:
        """
        ipv4:
        1） 4个数字3个点， 数字范围是0-255
        2） 除了0以外，所有数字不能以0开头，而且数字0只能是一个字符组成的字符串
        3） 与1， 2 冲突的都是false， 相反的都是true

        IPv6：
        1） 8个数字， 7个'：'
        2）每个数字都是16进制数字，每个数字最长4位，但是不能是0位长
        3） 与上面冲突的，都是false， 否则都是true

        IPv4 & IPv6 are both IP addresses that are binary numbers. I
        Pv4 is 32 bit binary number while IPv6 is 128 bit binary number address.
        IPv4 address are separated by periods while IPv6 address are separated by colons.

        Both are used to identify machines connected to a network.
        In principle, they are the same, but they are different in how they work.

        IPv4 32 bit, 32 / 4 = 8 , 4 段， SO 数字范围是 2 ^ 8 - 1 = 255
        IPv6 128 bit , 128 / 8 = 16, 8 段， so 数字范围是 2 ^ 16 - 1 = 65535
        :param IP:
        :return:
        """
        if IP is None:
            return 'Neither'

        parts = IP.split('.')
        if len(parts) == 4:
            for part in parts:
                try:
                    part_int = int(part)
                except ValueError:
                    return 'Neither'
            # if part_int < 0 or part_int > 255 or (part_int == 0 and len(part) != 1) or (
            #         part_int != 0 and part_int // 10 ** (len(part) - 1) == 0):
                if part_int < 0 or part_int > 255 or (part != '0' and part_int // 10 ** (len(part) - 1) == 0):
                    return 'Neither'
            return 'IPv4'
        else:
            parts = IP.split(':')
            if len(parts) == 8:
                for part in parts:
                    if not part or len(part) > 4 or not part.isalnum():
                        return 'Neither'
                    try:
                        part_int = int(part, base=16)
                    except ValueError:
                        return 'Neither'
                    if part_int < 0 or part_int > 65535:
                        return 'Neither'
                return 'IPv6'
        return 'Neither'




