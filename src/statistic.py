from statisticitem import StatisticItem


class Statistic:
    def __init__(self, target_file, raw_data):
        self._total_value = reduce(lambda a, b: a + b, raw_data.values())
        self._file = target_file
        self._data = []
        for k, v in raw_data.items():
            self._data.append(
                StatisticItem(
                    key=k,
                    count=v,
                    freq_percent=100 * v / self._total_value,
                    log_file=target_file
                )
            )

    def print_top(self, freq_limit=5, show_examples=False):
        total_items = len(self._data)
        filtered_items = sorted(
            filter(lambda i: i.freq_percent >= freq_limit, self._data),
            key=lambda i: i.count,
            reverse=True
        )
        total_filtered_items = len(filtered_items)
        if self._total_value > 0:
            print(
                "Top %d/%d findings with occurrence >= %d%% (%d%% total):\n----------------------" % (
                    total_filtered_items,
                    total_items,
                    freq_limit,
                    reduce(
                        lambda a, b: a + b,
                        map(lambda x: x.freq_percent, filtered_items)
                    )
                )
            )
            for item in filtered_items:
                print "[%3d%%] %s => %s" % (item.freq_percent, item.key, item.count)
                if show_examples:
                    print "---\nExamples:\n%s\n---\n" % "\n".join(item.examples(3))
